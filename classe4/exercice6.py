#!/usr/bin/env python
"""
Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
"""
from datetime import datetime
from netmiko import ConnectHandler

PYNET1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    }

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    }

JUNIPER_SRX = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': '',
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
    start_time = datetime.now()
    for device in (PYNET1, PYNET2, JUNIPER_SRX): 
        pynet_rtr = ConnectHandler(**device)
        output = command(pynet_rtr, "show arp")
        print
        print "Device: {} ========> {}".format(pynet_rtr.find_prompt(),\
        pynet_rtr.ip)
        print output
        print '*'*80
    print "\n"*2
    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)
    print "\n"*2
if __name__ == "__main__":
    main()



