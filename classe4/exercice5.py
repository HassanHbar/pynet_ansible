
#!/usr/bin/env python
"""
Use Netmiko to enter into configuration mode on pynet-rtr2.
Also use Netmiko to verify your state
(i.e. that you are currently in configuration mode).
"""
from getpass import getpass
from netmiko import ConnectHandler
PASSWORD = getpass()


PYNET1 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    }
def router_mode(rtr):
    """
    verify configuration mode
    """
    output = rtr.find_prompt()
    if rtr.check_config_mode():
        print output + " \n" + "Router is on Config mode"

def main():
    """
    se Netmiko to enter into configuration mode on pynet-rtr2.
    Also use Netmiko to verify your state
    (i.e. that you are currently in configuration mode).
    """
    pynet_rtr1 = ConnectHandler(**PYNET1)
    pynet_rtr1.config_mode()
    router_mode(pynet_rtr1)

if __name__ == "__main__":
    main()
