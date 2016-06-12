#!/usr/bin/env python
"""
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
"""
from getpass import getpass
from netmiko import ConnectHandler
PASSWORD = getpass()

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '50.76.53.27',
    'username': 'pyclass',
    'password': PASSWORD,
    'port': 8022,
    }



def command(rtr, cmd):
    """
    Send command down in the chanel
    """
    cmd = cmd.strip()
    outp = rtr.send_command(cmd)
    return rtr.find_prompt() + "\n" + outp + "\n"

def config(rtr, cmd):
    """
    Send config command down in the chanel
    """
    cmd = cmd.strip()
    config_command = [cmd]
    outp = rtr.send_config_set(config_command)
    return rtr.find_prompt() + "\n" + outp + "\n"

def main():
    """
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    """
    pynet_rtr2 = ConnectHandler(**PYNET2)
    output = config(pynet_rtr2, "logging buffered 16000")
    print output
    output = command(pynet_rtr2, " sh runn | in logging")
    print output


if __name__ == "__main__":
    main()



