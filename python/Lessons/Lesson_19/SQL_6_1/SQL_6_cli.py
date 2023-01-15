import argparse
from SQL_6 import IMDB
from pprint import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Top IMDB Movies Search",
        description="The program allows to search IMDB top 250 movies",
        epilog="By, Daniel Raz",
    )

    parser.add_argument("-n", "--name", help="the movie name to search")

    parser.add_argument(
        "-r", "--rating", action="store", help="The movie rating to filter by"
    )

    args = parser.parse_args()

    db = IMDB()

    if args.rating is None:
        pprint(db.contains(args.name))
    else:
        pprint(db.filter_by_rating(args.rating))
