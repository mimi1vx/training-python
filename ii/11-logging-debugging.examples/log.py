import sys
import argparse

import logging
logging.basicConfig(format="%(message)s", level=logging.INFO)

log = logging.getLogger()

if __name__ == '__main__':
    log.info("Hello.")
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", action="store_true", help="Turn on debugging")
    args = parser.parse_args()

    if args.debug:
        log.setLevel(logging.DEBUG)

    log.debug("sys.argv = {}, args = {}".format(sys.argv, args))

    log.info("Goodbye.")
