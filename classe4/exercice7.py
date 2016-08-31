#!/usr/bin/env python
"""
Use Netmiko to change the logging buffer size (logging buffered <size>) on pynet-rtr2.
"""
from getpass import getpass
from netmiko import ConnectHandler
PASSWORD = getpass()

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': PASSWORD,
    }



def send_command(rtr, cmd, config=0):

    """
    Send command down in the chanel
    """
    output = "\n" + "*"*80 + "\n"
    output += ''' Outputs in device "{0}" for the command\
    "{1}" is : \n'''.format(rtr.find_prompt(), cmd)
    output += "*"*80 + "\n"
    if config == 1:
        configs = []
        configs.append(cmd)
        output += rtr.send_config_set(configs)
    else:
        output += rtr.send_command(cmd)
    output += "\n" + "#"*80
    return output


def main():
    """
    Use Netmiko to execute 'show arp' on pynet-rtr2.
    """
    pynet_rtr2 = ConnectHandler(**PYNET2)
    print send_command(pynet_rtr2, "logging buffered 16000", 1)
    print send_command(pynet_rtr2, " sh runn | in logging")


if __name__ == "__main__":
    main()



