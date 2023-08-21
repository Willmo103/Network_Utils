# Filepath: /app/__init__.py
# Module: app
"""
__init__.py
Filepath: /app/__init__.py
Module: app
"""
import os

# Determine the root path of the app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# if this is installed as a dependency, the config file will be in the root of the project
# if this is run as a standalone project, the config file will be in the root of the app
if os.path.exists(os.path.join(APP_ROOT, "net-utils.config.json")):
    CONFIG_PATH = os.path.join(APP_ROOT, "net-utils.config.json")
else:
    CONFIG_PATH = os.path.join(os.path.dirname(APP_ROOT), "net-utils.config.json")
print("config path ", CONFIG_PATH)
print("app root ", APP_ROOT)
# load the environment variables
from .utils.json_utils import init_json as init_json, read_json as read_json
