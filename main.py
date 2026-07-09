import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("latitude",  help="Your latitude")
    parser.add_argument("longitude", help="Your longitude")
    args = parser.parse_args()
    print(f"LAT: {args.latitude}  LON: {args.longitude}")

if __name__ == "__main__":
    main()