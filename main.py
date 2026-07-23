import argparse
from celestialtracker.celestialtracker import CelestialTracker
from celestialtracker.tleloader import TLELoader

TLE_ENDPOINT = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
TLE_FILE = "tle_data.tle"
DEFAULT_SATELLITE_INDEX = 0


# TLE download demo
td = TLELoader(TLE_ENDPOINT,TLE_FILE)
#td.downloadTLE()
    
def showSatellites():
    satellites = td.getSatellites()
    print ("Satellites:")

    for index, satellite in enumerate(satellites) :
        print(f"{index}\t{satellite.name}")


def main():
    parser = argparse.ArgumentParser()
    # Mandatory positional arguments
    parser.add_argument("latitude",  help="Your latitude")
    parser.add_argument("longitude", help="Your longitude")

    # Optional flags
    parser.add_argument("-d","--date", help="The date for wich you want to get the satellite passes forecast (empty for current date) (format: yyyy-mm-dd)", default="",type=str)

    parser.add_argument("-e","--elevation", help="Elevation (in meters) from the wgs84 reference ellipsoid", default=20, type=float)

    parser.add_argument("-a","--horizon_altitude", help="Degrees above the horizon", default=10, type=float)

    parser.add_argument('-l', '--list_satellites', action='store_true', help="Shows satellites contained in the TLE file")  

    parser.add_argument("-s","--satellite", help="Satellite index in the TLE file", default=0, type=int)


    args = parser.parse_args()
    if args.list_satellites == True:
        showSatellites()
        return

    print(f"LAT: {args.latitude}  LON: {args.longitude}")


    latitude = float(args.latitude)
    longitude = float(args.longitude)

    c = CelestialTracker()
    predictions = c.getISSPredictions(latitude, longitude,args.elevation,args.horizon_altitude,args.date)
    
    print("----\n\n")

    print(predictions)

    print("----\n\n")
    

if __name__ == "__main__":
    main()