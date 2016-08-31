#!/usr/bin/env python
'''
Use the PyEZ load() method to set the hostname of the SRX using set, conf (curly brace)
After load(), display the differences between the running config and the candidate config
Additionally, perform at least one commit and one rollback(0) in this program.
'''

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from getpass import getpass

def main():

    '''
    I will test the case with applying config for 1 minute
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
        cfg = Config(a_device)
        cfg.lock()
        cfg.load(path="exercice4_config.xml" , format="xml", merge=True)
        print "#"*80
        print "Displaying the differences between the running config and the candidate config:"
        print "#"*80
        cfg.pdiff()
        print "+"*80
        print "Applying config"
        print "+"*80
        cfg.commit(comment="Applying config from exercice4_config.xml")
        print "-"*80
        print "reverting config back"
        cfg.rollback(1)
        cfg.pdiff()
        cfg.commit()
        print "-"*80
        print "\n"*2
        print
    except:
        print
        print "Authentication Error"
        print

if __name__ == "__main__":
    main()
