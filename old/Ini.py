import configparser
import os


def write_ini_file():
    config = configparser.ConfigParser()
    config.read("%s/settings.ini" % os.path.dirname(__file__))
    return config
