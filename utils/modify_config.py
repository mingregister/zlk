import sys
import os
import time

try:
    from configparser import ConfigParser
except:
    from ConfigParser import ConfigParser

from django.conf import settings


ConfigFile = settings.CONFIGFILE 

def read_config(field, key):
    cf = ConfigParser()
    try:
        cf.read(ConfigFile)
        result = cf.get(field, key)
    except:
        sys.exit(1)
    return result

def write_config(field, key, value):
    cf = ConfigParser()
    try:
        cf.read(ConfigFile)
        result = cf.get(field, key)
    except:
        sys.exit(1)
    return result


def write_config(config_file_path=None, field=None, key=None, value=None):
    cf = ConfigParser()
    try:
        cf.read(config_file_path)
        cf.set(field, key, value)
        cf.write(open(config_file_path,'w'))
    except:
        sys.exit(1)
    return True
    cf = ConfigParser()
    try:
        cf.read(config_file_path)
        cf.set(field, key, value)
        cf.write(open(config_file_path,'w'))
    except:
        sys.exit(1)
    return True
