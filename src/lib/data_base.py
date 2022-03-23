import os
from lib.log import logging


DATA_FOLDER = "../data"


def read_filedata(filename):
    filepath = os.path.join(DATA_FOLDER, filename)
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        x = f.read()
    return eval(x)


def save_filedata(filename, data):
    filepath = os.path.join(DATA_FOLDER, filename)
    with open(filepath, "w") as f:
        f.write(str(data))


def del_filedata(filename, key):
    data = read_filedata(filename)
    data.pop(key, None)
    save_filedata(filename, data)


def set_filedata(filename, key, value):
    data = read_filedata(filename)
    data[key] = value
    save_filedata(filename, data)


def get_filedata(filename, key, alt_value=None):
    data = read_filedata(filename)
    return data.get(key, alt_value)


def has_filedata(filename, key):
    data = read_filedata(filename)
    return key in data


def is_filedata(filename, key, value):
    return get_filedata(filename, key) == value
