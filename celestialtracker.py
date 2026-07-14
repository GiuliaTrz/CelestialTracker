import time

class CelestialTracker:
    def __init__(self):
        self._times = None
        self._events = None
        self._satellite = None
        self._observer = None
        pass

    def getISSPredictions(self, latitude : float, longitude : float, timestamp : int = None):
        if timestamp is None:
            timestamp = int(time.time())
        
        print(f"DEBUG : Using timestamp: {timestamp}")

        
        return

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