import sys
sys.path.append('src')

import unittest
from unittest.mock import patch, mock_open
from app.net_util import NetUtil, ConfigError

class TestNetUtil(unittest.TestCase):

    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    def test_init(self):
        nu = NetUtil()
        self.assertEqual(nu.ip_list, ['1.1.1.1'])

    # Remove the class level mock since you're mocking inside the function
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    def test_read_config_json(self):
        with patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}')):
            nu = NetUtil()  # Moved this inside the patch to ensure mocked open is used
            data = nu._read_config_json()
        self.assertEqual(data, {"ip_list": ['1.1.1.1']})

    # Same as above
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    def test_load_ip_list(self):
        with patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}')):
            nu = NetUtil()
            ips = nu._load_ip_list()
        self.assertEqual(ips, ['1.1.1.1'])

    # Add read_data for the mock
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    def test_add_ip(self):
        nu = NetUtil()
        nu.add_ip("2.2.2.2")
        self.assertIn("2.2.2.2", nu.ip_list)

    # Add read_data for the mock
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    def test_save(self):
        nu = NetUtil()
        nu.save()

    # Add read_data for the mock
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    def test_repr(self):
        nu = NetUtil()
        representation = repr(nu)
        self.assertIsInstance(representation, str)

    # Rest remain the same since they are already providing read_data
    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    @patch("app.net_util.ping", return_value=None)
    def test_run_ping_ips_unreachable(self, mock_ping):
        nu = NetUtil()
        with patch("logging.error") as mock_log:
            nu.run_ping_ips()
            mock_log.assert_called_once_with("1.1.1.1 is unreachable.")

    @patch("os.environ", {"CONFIG_PATH": "mock_path"})
    @patch("builtins.open", mock_open(read_data='{"ip_list": ["1.1.1.1"]}'))
    @patch("app.net_util.ping", return_value=20)  # returning any non-None value to simulate reachability
    def test_run_ping_ips_reachable(self, mock_ping):
        nu = NetUtil()
        with patch("logging.info") as mock_log:
            nu.run_ping_ips()
            mock_log.assert_called_once_with("1.1.1.1 is reachable.")

if __name__ == "__main__":
    unittest.main()
