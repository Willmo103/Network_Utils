# Filepath: \app\net_util.py
# File: net_util.py
# Module: app

import json
import os

class ConfigError(Exception):
    """An exception to be raised when there is an error with the config file"""
    pass

class NetUtil:
    """A class to handle the ip address list and config file

    Attributes:
        path (str): the path to the config file
        ip_list (list): the list of ip addresses to scan

        Methods:
            read_json: reads a json file at the given path
            load_ip_list: loads the ip address list from the config file
            add_ip: adds an ip address to the ip address list
            save: saves the ip address list to the config file

            Raises:
                ConfigError: raised when there is an error with the config file

    """
    def __init__(self):
        self.path = os.environ.get("CONFIG_PATH")
        self.ip_list = self._load_ip_list()
        data = {"ip_list": self.ip_list}
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def _read_config_json(self) -> dict:
        """Reads a json file at the given path
        :param path: the path to read the json file from
        :return: the data from the json file
        """
        try:
            with open(self.path, "r") as f:
                data = json.load(f)
            return data
        except FileNotFoundError as e:
            print("No config file found. run 'net-utils init' to create one")
            raise ConfigError("Error reading config file")

    def _load_ip_list(self) -> list:
        """Loads the ip address list from the config file
        :return: the ip address list
        """
        try:
            data = self._read_config_json()
            return data["ip_list"]
        except FileNotFoundError as e:
            return []

    def add_ip(self, address: str) -> list:
        self.ip_list.append(address)
        self.save()
        return self.ip_list

    def save(self):
        data = self._read_config_json()
        data["ip_list"] = self.ip_list
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def __repr__(self) -> str:
        return (
            "NetUtil("
            f"path={self.path}, "
            f"ip_list={self.ip_list}"
        )

    @classmethod
    def from_json(cls, path: str) -> "NetUtil":
        """Creates a NetUtil object from a json file
        :param path: the path to the json file
        :return: a NetUtil object
        """
        data = cls._read_config_json(path)
        return cls(data["ip_list"])

    def run_ping_ips(self):
        """Ping all the ip addresses in the ip address list
        log the results to a file
        """
        for ip in self.ip_list:
            os.system(f"ping {ip} >> ping.log")

