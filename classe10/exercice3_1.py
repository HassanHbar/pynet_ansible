#!/usr/bin/env python

'''
splay the SRX's routing table. You will probably want to use RouteTable for this
(from jnpr.junos.op.routes import RouteTable). The output should look similiar
to the following:
Juniper SRX Routing Table:

0.0.0.0/0
  nexthop 10.220.88.1
  age 14582542
  via vlan.0
  protocol Static

10.220.88.0/24
  nexthop None
  age 14583120
  via vlan.0
  protocol Direct

10.220.88.39/32
  nexthop None
  age 14583289
  via vlan.0
  protocol Local
'''

from jnpr.junos import Device
from jnpr.junos.op.routes import RouteTable
from getpass import getpass

def main():
    '''
    Formatting the routing table
    '''
    pwd = getpass()
    try:
        a_device = Device(host='184.105.247.76', user='pyclass', password=pwd)
        a_device.open()
        route_table = RouteTable(a_device)
        route_table.get()
        print "\n"*2
        print "Juniper SRX Routing Table: \n"
        for route, route_att in route_table.items():
            print route
            for desc, value in route_att:
                print ("\t {0} {1}").format(desc, value)
            print "\n"
        print
    except:
        print
        print "Authentication Error"
        print

if __name__ == "__main__":
    main()
