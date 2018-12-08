from __future__ import print_function

import argparse
import logging.handlers
import os
import configparser
from thgconsole.interpreter import THGtInterpreter

# Define conf
thg_conf_file = "thg.ini"
thg_conf = configparser.ConfigParser(allow_no_value=True)
thg_conf.read(thg_conf_file)

# Get parameter from conf
log_file_name = thg_conf.get("LOG", "log_file_name")
log_max_bytes = thg_conf.getint("LOG", "log_max_bytes")
log_level = thg_conf.getint("LOG", "log_level")
package_path = thg_conf.get("EXTRA_PACKEAGE", "package_path")


# Define logger
log_handler = logging.handlers.RotatingFileHandler(filename=log_file_name, maxBytes=log_max_bytes)
log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s       %(message)s')
log_handler.setFormatter(log_formatter)
LOGGER = logging.getLogger()
LOGGER.setLevel(log_level)
LOGGER.addHandler(log_handler)

parser = argparse.ArgumentParser(description='THG - the hacker group ')
parser.add_argument('-e',
                    '--extra-package-path',
                    metavar='extra_package_path',
                    help='Add extra packet(modules) to thg.')


def thg(extra_package_path=package_path):
    if not os.path.isdir(extra_package_path):
        extra_package_path = None
    thgc = THGtInterpreter(extra_package_path)
    thgc.start()


if __name__ == "__main__":
    args = parser.parse_args()
    if args.extra_package_path:
            thg(extra_package_path=args.extra_package_path)
    else:
        thg()
