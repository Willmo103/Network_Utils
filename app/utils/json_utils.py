import json
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

class ConfigError(Exception):
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

def load_ip_address_list() -> list:
    """Loads the ip address list from the config file
    :return: the ip address list
    """
    data = read_json("config.json")
    return data["ip_address_list"]
