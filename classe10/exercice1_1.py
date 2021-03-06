#!/usr/bin/env python

'''
Use Juniper's PyEZ library to make a connection to the Juniper SRX and
to print out the device's facts
'''

from jnpr.junos import Device
from pprint import pprint
from getpass import getpass

def main():
    '''
    Use Juniper's PyEZ library to make a connection to the Juniper SRX and
    to print out the device's facts
    '''
    pwd = getpass()
    ip_addr = raw_input('''Enter Juniper SRX IP"(184.105.247.76)": ''')
    ip_addr = ip_addr.strip()
    juniper_srx = {
        "host": ip_addr,
        "user": "pyclass",
        "password": pwd
    }
    try:
        a_device = Device(**juniper_srx)
        a_device.open()
        print "\n"*2
        pprint(a_device.facts)
        print
    except:
        print
        print "Authentication Error"
        print

if __name__ == "__main__":
    main()
