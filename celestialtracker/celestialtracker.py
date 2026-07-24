from datetime import datetime, timedelta, timezone
from skyfield.api import load, EarthSatellite, utc, wgs84
from datetime import datetime, timedelta, timezone
from satelles import TLE
import time

class CelestialTracker:

    def __init__(self, satellite : EarthSatellite):
        self._times = None
        self._events = None
        self._satellite = satellite
        self._observer = None
        pass

    def getISSPredictions(self, latitude : float, longitude : float, elevation_meters : float = 20, altitude_degrees : float = 10.0, date : str = ""):
        if date == "":
            date = datetime.now(timezone.utc) + timedelta(days=1)
        else:
            date = datetime.strptime(date, "%Y-%m-%d").replace(
                tzinfo=timezone.utc
            )


        ts = load.timescale()


        self._observer = wgs84.latlon(
            latitude_degrees=latitude,
            longitude_degrees=longitude,
            elevation_m=elevation_meters
        )

        t = ts.now();


        tMax = ts.from_datetime(
            date
        )

        self._times, self._events = self._satellite.find_events(self._observer, t, tMax, altitude_degrees=altitude_degrees)
        
        return self._getDataObject()

    def azimuth_to_cardinals(self, az):
        directions = [
            "N", "NNE", "NE", "ENE",
            "E", "ESE", "SE", "SSE",
            "S", "SSW", "SW", "WSW",
            "W", "WNW", "NW", "NNW"
        ]
        index = round(az / 22.5) % 16
        return directions[index]

    def _getDataObject(self):
        times = self._times
        events = self._events
        data = {"events": []}
        current_event = None

        names = [
            "START",
            "MAX",
            "END"
        ]

        for t, e in zip(times, events):
            difference = self._satellite - self._observer
            topocentric = difference.at(t)
            alt, az, distance = topocentric.altaz()

            dt = t.utc_datetime().astimezone()

            phase = {
                "type": names[e].strip().upper(),
                "timestamp": dt.strftime("%d/%m/%Y %H:%M:%S"),
                "elevation": round(float(alt.degrees), 1),
                "azimuth": round(float(az.degrees), 1),
                "cardinal": self.azimuth_to_cardinals(az.degrees),
                "distance": round(float(distance.km), 3)
            }

            if phase["type"] == "START":
                current_event = {
                    "event_time": phase["timestamp"],
                    "phases": [phase]
                }

            elif current_event is not None:
                current_event["phases"].append(phase)

                if phase["type"] == "END":
                    data["events"].append(current_event)
                    current_event = None

        return data