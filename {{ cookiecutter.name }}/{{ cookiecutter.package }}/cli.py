import argparse
import os
import sys
import logging
from . import __version__

j = os.path.join


ARGS = argparse.ArgumentParser()
ARGS.add_argument("--version",
                  action="version",
                  version="%(prog)s " + __version__,
                  )
ARGS.add_argument("-d", "--debug",
                  action="store_true",
                  help="set debug/development mode on"
                  )


def main(argv=sys.argv[1:]):
    args = ARGS.parse_args(argv)
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
