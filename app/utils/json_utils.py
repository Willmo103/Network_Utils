"""
A module to handle the json config file
Filepath: /app/utils/json_utils.py
Module: app.utils.json_utils

functions:
    init_json(path: str) -> bool or ConfigError
    read_json(path: str) -> dict
    load_ip_address_list() -> list

classes:
    ConfigError(Exception)

"""
import json
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# create a base url for net-utils.config.json
#  - get the root of the application location

class ConfigError(Exception):
    """An exception to be raised when there is an error with the config file"""
    pass

# a function to create the config json file on install
def init_json(path: str) -> bool or ConfigError:
    """Creates a json file at the given path
    :param path: the path to create the json file at
    :return: True if the file was created, False otherwise
    """
    try:
        with open(path, "w") as f:
            json.dump({}, f, indent=4)
        return True
    except Exception as e:
        print("Unable to create config file")
        raise ConfigError("Error creating config file")

# a function to read the config json file
def read_json(path: str) -> dict:
    """Reads a json file at the given path
    :param path: the path to read the json file from
    :return: the data from the json file
    """
    try:
        with open(path, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError as e:
        print("No config file found. run 'net-utils init' to create one")
        raise ConfigError("Error reading config file")

# a function to write to the config json file
def load_ip_address_list(path: str) -> list:
    """Loads the ip address list from the config file
    :return: the ip address list
    """
    data = read_json(path)
    return data["ip_address_list"]

def save_ip_address_list(path: str, ip_address_list: list) -> None:
    """Saves the ip address list to the config file
    :param ip_address_list: the ip address list to save
    """
    data = read_json(path)
    data["ip_address_list"] = ip_address_list
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
