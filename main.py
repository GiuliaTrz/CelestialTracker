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

def getSatellitePredictions(satelliteIndex, latitude, longitude,elevation,horizon_altitude,date):
    satellites = td.getSatellites()

    print(f"Satellite Index: {satelliteIndex}")
    print(f"Satellite      : {satellites[satelliteIndex]}")

    c = CelestialTracker()
    predictions = c.getISSPredictions(latitude, longitude,elevation,horizon_altitude,date)
    
    print("----\n\n")

    print(predictions)

    print("----\n\n")

def main():
    parser = argparse.ArgumentParser()

    # Optional flags
    parser.add_argument("-d","--date", help="The date for wich you want to get the satellite passes forecast (empty for current date) (format: yyyy-mm-dd)", default="",type=str)

    parser.add_argument("-e","--elevation", help="Elevation (in meters) from the wgs84 reference ellipsoid", default=20, type=float)

    parser.add_argument("-a","--horizon_altitude", help="Degrees above the horizon", default=10, type=float)

    parser.add_argument('-l', '--list_satellites', action='store_true', help="Shows satellites contained in the TLE file")  

    parser.add_argument("-s","--satellite", help="Satellite index in the TLE file", default=0, type=int)

    parser.add_argument("latitude", nargs="?", type=float)
    parser.add_argument("longitude", nargs="?", type=float)

    args = parser.parse_args()
    if args.list_satellites == True:
        showSatellites()
        return
    else:
        if args.latitude is None or args.longitude is None:
            parser.error("latitude and longitude are required unless -l is specified")
            
        print(f"LAT: {args.latitude}  LON: {args.longitude}")

        latitude = float(args.latitude)
        longitude = float(args.longitude)

        getSatellitePredictions(args.satellite, latitude, longitude,args.elevation,args.horizon_altitude,args.date)
    

if __name__ == "__main__":
    main()