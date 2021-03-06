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

#This constant permit us to know if there is a change during the first 
# 5 minutes
RELOAD_WINDOW = 30000

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


def extract_snmp_data_from_devices(a_device):
    '''
    extract SNMP data (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED) from each
    device and pack it  in the list called snmp_results []
    '''
    RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
    SYS_NAME = '1.3.6.1.2.1.1.5.0'
    SYS_UPTIME = '1.3.6.1.2.1.1.3.0'
    snmp_results = []
    for oid  in (SYS_NAME, SYS_UPTIME, RUN_LAST_CHANGED):
            try:
                value = snmp_extract(snmp_get_oid_v3(a_device, snmp_user, oid=oid))
                snmp_results.append(int(value))
            except ValueError:
                snmp_results.append(value)
    return snmp_results

def extract_saved_data(file_name):
    '''
    extract saved data from the pickle file
    '''
    # Check that the pickle file exists

    DEBUG1 = True
    if not  os.path.isfile(file_name):
        return {}
    
    # if the pickle file is not empty return the content, if empy return an
    # empty dictionary
    net_devices = {}
    with open(net_dev_file, 'r') as f:
        while DEBUG1:
            try:
                net_devices = pickle.load(f)
                DEBUG1 = False
            except IOError:
                break
    return net_devices

def save_data_to_file(file_name, data_dict):
    
    '''
    this function store retreived data to the file_name
    '''
    if file_name.count(".") == 1:
        _,out_format = file_name.split(".")
    else:
        raise ValueError("Invalid file name: {0}".format(file_name))
    if out_format == 'pkl':
        with open(file_name, 'w') as f:
            pickle.dump(data_dict, f)

def email_notification(router, time):
    
    '''
    this function send an email notification to receptient indicating that
    an equipement has a configuration cahnge.
    '''
    
    
    sender = 'hassanh@mhdinfotech.com'
    recepient = 'hassanhbar@gmail.com'
    subject = router + ' has a configuration change at ' + str(datetime.timedelta(seconds=time/100))
    message = '''
    Hi,    
    this is to inform you that {0} had a configuration change at {1}.
    Best regards, 
    Hassan HBAR.
    '''.format(router, str(datetime.timedelta(seconds=time/100)))
    

    email_helper.send_mail(recepient, subject, message, sender)

def main():
    '''
    Check if the running-configuration has changed, send an email notification when
    this occurs. the logic here is the following:
    1) We extract saved data
    2) we request SNMP data
    3) We compare requested SNMP data and saved data to define if config was changed(
    I follow here same logic as your soluton)
    4) save SNMP data in the pickle file
    '''
    snmp_data = {}
    current_data = {}
    saved_data = extract_saved_data(net_dev_file)
    
    for a_device in (pynet_rtr1, pynet_rtr2):

        device_name, uptime, last_changed = extract_snmp_data_from_devices(a_device)
        current_data[device_name] = {'device_name':device_name,\
        'uptime':uptime, 'last_changed':last_changed}
        
        print "\nConnected to device = {0}".format(device_name)
        print "Last changed timestamp = {0}".format(last_changed)
        print "Uptime = {0}".format(uptime)
        
        # see if this device has been previously saved
        if device_name in saved_data.keys():
            snmp_saved_data = saved_data[device_name]
            print "{0} Already Saved {1}".format(device_name, (35 - len(device_name))*'.'),
            #Check for a reboot (did uptime decrease or last_changed decrease?)
            if uptime < snmp_saved_data['uptime'] or last_changed < snmp_saved_data['last_changed']:
                if last_changed <= RELOAD_WINDOW:
                    print "DEVICE RELOADED...not changed"
                else:
                    print "DEVICE RELOADED...and changed, email notification is sent"
                    email_notification(device_name, last_changed)
            # running-config last_changed is the same
            elif last_changed == snmp_saved_data['last_changed']:
                print "not changed"
            # running-config was modified
            elif last_changed > snmp_saved_data['last_changed']:
                print "CHANGED,  email notification is sent"
                email_notification(device_name, last_changed)
        else:
            # New device, just save it
            print "{0} {1}".format(device_name, (35 - len(device_name))*'.'),
            print "saving new device"
    
    # Write the devices to pickle file
    save_data_to_file(net_dev_file, current_data)

if __name__ == "__main__":
    main()
