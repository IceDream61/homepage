import os
import lib.log
from lib.data_base import set_filedata, get_filedata


USERINFOS_FILENAME = "userinfos"


def get_userinfo(username, key):
    info = get_filedata(USERINFOS_FILENAME, username, {})
    return info.get(key)


def set_userinfo(username, key, value):
    info = get_filedata(USERINFOS_FILENAME, username, {})
    info[key] = value
    set_filedata(USERINFOS_FILENAME, username, info)
