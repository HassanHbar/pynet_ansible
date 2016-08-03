#!/usr/bin/env python
'''
Using SNMPv3 create a script that detects router configuration changes.
If the running configuration has changed, then send an email notification to
identifying the router that changed and the time that it changed.
'''

import cPickle as pickle
import datetime
import os.path
import email_helper
from snmp_helper import snmp_get_oid_v3, snmp_extract

DEBUG = True
RELOAD_WINDOW = 300 * 100
RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
SYS_NAME = '1.3.6.1.2.1.1.5.0'
SYS_UPTIME = '1.3.6.1.2.1.1.3.0'

ip_addr1 = "184.105.247.70"
ip_addr2 = "184.105.247.71"
a_user = 'pysnmp'
my_key = "galileo1"
auth_key = my_key
encrypt_key = my_key
snmp_user = (a_user, auth_key, encrypt_key)
pynet_rtr1 = (ip_addr1, 161)
pynet_rtr2 = (ip_addr2, 161)
net_dev_file = 'netdev.pkl'


def extract_saved_devices(file_name):
    '''
    extract saved data in pickle file
    '''
    # Check that the pickle file exists
    if not  os.path.isfile(file_name):
        return {}
    net_devices = {}
    with open(net_dev_file, 'r') as f:
        while True:
            try:
                tmp_device = pickle.load(f)
                net_devices[tmp_device['device_name']] = tmp_device
            except EOFError:
                break
    return net_devices


def email_notification(router, time):
    '''
    this function send an email notification to receptient indicating that
    an equipement has a configuration cahnge.
    '''
    sender = 'hassanh@mhdinfotech.com'
    recepient = 'hassanhbar@gmail.com'
    subject = router + ' has a configuration change at ' + str(datetime.timedelta(time/100))
    message = '''
Hi,    
this is to inform you that {0} had a configuration change at {1}.
Best regards, 
Hassan HBAR.
    '''.format(router, time)
    email_helper.send_mail(recepient, subject, message, sender)

def main():
    '''
    Check if the running-configuration has changed, send an email notification when
    this occurs.
    '''
    current_devices = {}
    saved_devices = extract_saved_devices(net_dev_file)
    print "{0} devices were previously saved\n".format(len(saved_devices))
    for a_device in (pynet_rtr1, pynet_rtr2):
        snmp_results = []
        for oid  in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            try:
                value = snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid))
                snmp_results.append(int(value))
            except ValueError:
                snmp_results.append(value)

        device_name, uptime, last_changed = snmp_results
        current_devices[device_name] = {'device_name':device_name,\
 'uptime':uptime, 'last_changed':last_changed}
        if DEBUG:
            print "\nConnected to device = {0}".format(device_name)
            print "Last changed timestamp = {0}".format(last_changed)
            print "Uptime = {0}".format(uptime)
        # see if this device has been previously saved
        if device_name in saved_devices:
            saved_device = saved_devices[device_name]
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),
            # Check for a reboot (did uptime decrease or last_changed decrease?)
            if uptime < saved_device['uptime'] or last_changed < saved_device['last_changed']:
                if last_changed <= RELOAD_WINDOW:
                    print "DEVICE RELOADED...not changed"
                else:
                    print "DEVICE RELOADED...and changed"
                    email_notification(device_name, last_changed)

            # running-config last_changed is the same
            elif last_changed == saved_device['last_changed']:
                print "not changed"
            # running-config was modified
            elif last_changed > saved_device['last_changed']:
                print "CHANGED"
                email_notification(device_name, last_changed)
        else:
            # New device, just save it
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),
            print "saving new device"
    # Write the devices to pickle file
    with open(net_dev_file, 'w') as f:
        for dev_obj  in current_devices.values():
            pickle.dump(dev_obj, f)

if __name__ == "__main__":
    main()
