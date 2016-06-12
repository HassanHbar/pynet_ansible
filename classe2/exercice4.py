#!/usr/bin/env python


from snmp_helper import snmp_get_oid,snmp_extract

community = 'galileo'
port1 = 7961
port2 = 8061
IP = "50.76.53.27"



rtr1 = (IP, community, port1)
rtr2 = (IP, community, port2)

OID_SysName = '1.3.6.1.2.1.1.1.0'
OID_SysDescr = '1.3.6.1.2.1.1.5.0'

def snmp_request(host, OID):
    snmp_data = snmp_get_oid(host, OID)
    output = snmp_extract(snmp_data)
    print output

def main():
    print "========================================================"
    snmp_request(rtr1, OID_SysDescr)
    print "========================="
    snmp_request(rtr1, OID_SysName)
    
    print "========================================================"
    snmp_request(rtr2, OID_SysDescr)
    print "========================="
    snmp_request(rtr2, OID_SysName)




if __name__ == "__main__":
    main()

 

