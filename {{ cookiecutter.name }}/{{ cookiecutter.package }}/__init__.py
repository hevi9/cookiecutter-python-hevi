import pkg_resources
import sys
import logging


NAME = "{{cookiecutter.name}}"
try:
    __version__ = pkg_resources.get_distribution(NAME).version
except pkg_resources.DistributionNotFound:
    __version__ = "0.0.0"


log = logging.getLogger(NAME)
D = log.debug
