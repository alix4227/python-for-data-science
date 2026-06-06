import sys
from antigravity import geohash


def main(args):
    geohash(float(args[1]), float(args[2]), args[3].encode())

if __name__ == "__main__":
    main(sys.argv)