import os, logging
# Determine the root path of the app
APP_ROOT = os.path.dirname((os.path.abspath(__file__)))

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

log_path = os.path.join(APP_ROOT, "net-utils.log")
logging.basicConfig(filename=log_path, level=logging.DEBUG, format="%(asctime)s %(levelname)s %(name)s %(message)s")
logger = logging.getLogger(__name__)
