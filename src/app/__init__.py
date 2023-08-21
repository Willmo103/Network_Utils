# Filepath: /app/__init__.py
# Module: app
import json, os

# Determine the root path of the app
APP_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(APP_ROOT)
# if this is installed as a dependency, the config file will be in the root of the project
# if this is run as a standalone project, the config file will be in the root of the app
if os.path.exists(os.path.join(APP_ROOT, "net-utils.config.json")):
    CONFIG_PATH = os.path.join(APP_ROOT, "net-utils.config.json")
else:
    CONFIG_PATH = os.path.join(os.path.dirname(APP_ROOT), "net-utils.config.json")

# set the environment variables
os.environ["CONFIG_PATH"] = CONFIG_PATH
os.environ["APP_ROOT"] = APP_ROOT

# create the config file if it doesn't exist
if not os.path.exists(CONFIG_PATH):
    with open(CONFIG_PATH, "w") as f:
        f.write('{ "ip_list": [] }')

# import the modules
from .net_util import NetUtil

# nu = NetUtil()
# print(nu._load_ip_list())
# new_ip = input("enter an IP address to add to the list: ")
# print(nu.add_ip(new_ip))
# nu.run_ping_ips()

