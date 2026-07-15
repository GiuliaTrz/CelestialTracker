import argparse
from celestialtracker.celestialtracker import CelestialTracker
from celestialtracker.tleloader import TLELoader
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("latitude",  help="Your latitude")
    parser.add_argument("longitude", help="Your longitude")
    args = parser.parse_args()
    print(f"LAT: {args.latitude}  LON: {args.longitude}")

    latitude = float(args.latitude)
    longitude = float(args.longitude)

    c = CelestialTracker()
    predictions = c.getISSPredictions(latitude, longitude)
    
    print(predictions)

    # TLE download demo
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
    file = "output.txt"
    td = TLELoader(url,file)
    print(td.getSatellites())
    print(td.downloadTLE())
    print(td.getSatellites())
    

if __name__ == "__main__":
    main()