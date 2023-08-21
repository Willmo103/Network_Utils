from app.net_util import NetUtil

def test_add_ip():
    nu = NetUtil()
    initial_length = len(nu.ip_list)
    nu.add_ip("192.168.1.1")
    assert len(nu.ip_list) == initial_length + 1

def test_ping_ips():
    # You can mock the ping function or test on known IPs
    pass
