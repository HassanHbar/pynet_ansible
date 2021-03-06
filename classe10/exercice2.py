#!/usr/bin/env python

'''
For each of the SRX's interfaces, display: the operational state,
packets-in, and packets-out. You will probably want to use EthPortTable for
this.
'''

from jnpr.junos import Device
from jnpr.junos.op.ethport import EthPortTable
from getpass import getpass

def main():
    '''
    For each of the SRX's interfaces, display: the operational state,
    packets-in, and packets-out. You will probably want to use EthPortTable for
    this.
    '''
    pwd = getpass()
    try:
        a_device = Device(host='184.105.247.76', user='pyclass', password=pwd)
        a_device.open()
        ports = EthPortTable(a_device)
        ports.get()
        print "\n"*2
        for port in ports.keys():
            print "#"*80
            print "Operational state, Packets-in and Packets-out for Port {0} are :".format(port)
            print "#"*80
            print "Operational state is : {0}".format(ports[port]['oper'])
            print "Packets-in are : {0}".format(ports[port]['rx_packets'])
            print " Packets-out are : {0}".format(ports[port]['tx_packets'])
            print "*"*80
            print "\n"*2
        print
    except:
        print
        print "Authentication Error"
        print

if __name__ == "__main__":
    main()
