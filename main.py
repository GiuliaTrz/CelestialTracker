import argparse
from datetime import datetime, timedelta, timezone
import os
import sys
from celestialtracker.celestialtracker import CelestialTracker
from celestialtracker.tleloader import TLELoader
from prettytable import PrettyTable
import json
TLE_ENDPOINT = "https://celestrak.org/NORAD/elements/gp.php?GROUP=stations&FORMAT=tle"
TLE_FILE = "tle_data.tle"
DEFAULT_SATELLITE_INDEX = 0


td = TLELoader(TLE_ENDPOINT,TLE_FILE)

def initialize():
    if os.path.isfile(TLE_FILE) == False:
        downloadTLE()

def downloadTLE():
    try:
        print(f"[INFO] Downloading TLE data from {TLE_ENDPOINT}")
        rc = td.downloadTLE()
        if rc != 200:
            print(f"[ERROR] An error occurred during TLE update HTTP Return code: {rc}")
        else:
            print("[SUCCESS] TLE data updated, restart the application")
            sys.exit(0)
    except Exception as err:
        print(f"[ERROR] An error occurred during TLE update: Unexpected {err=}, {type(err)=}")

def checkTLEUpdate(satellite):
    if shouldUpdateTLE(satellite):
        print("/!\\ WARNING /!\\ TLE data older than 24 hours")
        print("[INFO] Trying to update TLE data...")
        downloadTLE()
    
def showSatellites():
    satellites = td.getSatellites()
    print ("Satellites:")

    for index, satellite in enumerate(satellites) :
        print(f"{index}\t{satellite.name}")

def shouldUpdateTLE(satellite) -> bool:
    """
    Returns True if the TLE file is older than 24 hours (UTC date time)
    """
    tle_date = satellite.epoch.utc_datetime()
    now = datetime.now(timezone.utc)
    return (now - tle_date) > timedelta(hours=24)

def printPrettyTable(predictions):
    for event in predictions["events"]: 
        print(f"Event: {event["event_time"]}")
        table = PrettyTable()
        table.field_names = ["Type", "Timestamp", "Elevation°", "Azimuth°", "Cardinal", "Distance (Km)"]
        for phase in event["phases"] : 
            table.add_row([phase["type"], phase["timestamp"], phase["elevation"], phase["azimuth"], phase["cardinal"], phase["distance"]])
        print(table)
        print()


def printAsJson(predictions):
    print(json.dumps(predictions))

def getSatellitePredictions(satelliteIndex, latitude, longitude,elevation,horizon_altitude,date, jsonFormat : bool):
    satellites = td.getSatellites()

    c = CelestialTracker(satellites[satelliteIndex])
    checkTLEUpdate(satellites[satelliteIndex]) # Checks for TLE update

    predictions = c.getISSPredictions(latitude, longitude,elevation,horizon_altitude,date)

    if jsonFormat:
        printAsJson(predictions)
    else:
        print ("\n")
        print(f"Satellite: {satellites[satelliteIndex]}")
        print ("\n")
        printPrettyTable(predictions)


def main():
    parser = argparse.ArgumentParser()

    # Optional flags
    parser.add_argument("-d","--date", help="The date for wich you want to get the satellite passes forecast (empty for current date) (format: yyyy-mm-dd)", default="",type=str)

    parser.add_argument("-e","--elevation", help="Elevation (in meters) from the wgs84 reference ellipsoid", default=20, type=float)

    parser.add_argument("-a","--horizon_altitude", help="Degrees above the horizon", default=10, type=float)

    parser.add_argument('-l', '--list_satellites', action='store_true', help="Shows satellites contained in the TLE file")  

    parser.add_argument("-s","--satellite", help="Satellite index in the TLE file", default=0, type=int)

    parser.add_argument('-j', '--json', action='store_true', help="Prints the satellite passes forecast using JSON format")  

    parser.add_argument("latitude", nargs="?", type=float)
    parser.add_argument("longitude", nargs="?", type=float)

    args = parser.parse_args()
    if args.list_satellites == True:
        initialize()
        showSatellites()
        return
    else:
        initialize()
        if args.latitude is None or args.longitude is None:
            parser.error("latitude and longitude are required unless -l is specified")

        if args.json != True:
            print ("\n")
            print(f"Latitude: {args.latitude}  Longitude: {args.longitude}")

        latitude = float(args.latitude)
        longitude = float(args.longitude)

        getSatellitePredictions(args.satellite, latitude, longitude,args.elevation,args.horizon_altitude,args.date, args.json)
    

if __name__ == "__main__":
    main()