import sys
from antigravity import geohash


def main(args):
    try:
        if len(args) != 4:
            raise ValueError("Invalid number of arguments. Usage: python geohashing.py <latitude> <longitude> <precision>")
        latitude = float(args[1])
        longitude = float(args[2])
        precision = args[3].encode()
        geohash(latitude, longitude, precision)
        return 1
    except ValueError as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    main(sys.argv)