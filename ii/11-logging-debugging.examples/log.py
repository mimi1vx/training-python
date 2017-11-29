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

    try:
        a = 1/0
    except:
        log.exception("things went wrong")
        #from traceback import format_exc
        #log.debug(format_exc())

    log.debug("sys.argv = {}, args = {}".format(sys.argv, args))

    log.info("Goodbye.")
