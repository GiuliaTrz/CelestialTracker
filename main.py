import argparse
from celestialtracker.celestialtracker import CelestialTracker
from celestialtracker.tleloader import TLELoader

TLE_ENDPOINT = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
TLE_FILE = "tle_data.tle"
DEFAULT_SATELLITE_INDEX = 0

def main():
    parser = argparse.ArgumentParser()
    # Mandatory positional arguments
    parser.add_argument("latitude",  help="Your latitude")
    parser.add_argument("longitude", help="Your longitude")

    # Optional flags
    parser.add_argument("-d","--date", help="The date for wich you want to get the satellite passes forecast (empty for current date) (format: yyyy-mm-dd)", default="",type=str)

    parser.add_argument("-e","--elevation", help="Elevation (in meters) from the wgs84 reference ellipsoid", default=20, type=float)

    parser.add_argument("-a","--horizon_altitude", help="Degrees above the horizon", default=10, type=float)

    args = parser.parse_args()
    print(f"LAT: {args.latitude}  LON: {args.longitude}")

    latitude = float(args.latitude)
    longitude = float(args.longitude)

    c = CelestialTracker()
    predictions = c.getISSPredictions(latitude, longitude,args.elevation,args.horizon_altitude,args.date)
    
    print("----\n\n")

    print(predictions)

    print("----\n\n")

    # TLE download demo
    td = TLELoader(TLE_ENDPOINT,TLE_FILE)
    #td.downloadTLE()
    print(td.getSatellites())
    

if __name__ == "__main__":
    main()