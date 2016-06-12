#!/usr/bin/env python
"""
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
"""
from getpass import getpass
from datetime import datetime
from netmiko import ConnectHandler
PASSWORD = getpass()


PYNET1 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    }

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    'port': 8022,
    }

JUNIPER_SRX = {
    'device_type': 'juniper',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    'secret': '',
    'port': 9822,
    }

def command(rtr, cmd):
    """
    Send command down in the chanel
    """
    cmd = cmd.strip()
    outp = rtr.send_command(cmd)
    return rtr.find_prompt() + "\n" + outp + "\n"

def main():
    """
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    """
    print "\nStart time: " + str(datetime.now())
    pynet_rtr1 = ConnectHandler(**PYNET1)
    pynet_rtr2 = ConnectHandler(**PYNET2)
    srx = ConnectHandler(**JUNIPER_SRX)
    output1 = command(pynet_rtr1, "show arp")
    print output1
    output2 = command(pynet_rtr2, "show arp")
    print output2
    output3 = command(srx, "show arp")
    print output3
    print "\nEnd time: " + str(datetime.now())

if __name__ == "__main__":
    main()



