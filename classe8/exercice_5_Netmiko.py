#!/usr/bin/env python
""" Week 8, exercice 5"""

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django

def show_version(a_device):
    creds= a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address, username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='')
    print
    print '#' * 80
    print remote_conn.send_command_expect("show version")
    print '#' * 80

def main():
    """Use Netmiko to connect to each of the devices in the database. Execute 'show version' on each device.
        Calculate the amount of time required to do this. Note, your results will be more reliable if you use 
        Netmiko's send_command_expect() method. There is an issue with the Arista vEOS switches and Netmiko's 
        send_command() method"""
    
    django.setup()
    devices = NetworkDevice.objects.all()
    start_time = datetime.now()

    for a_device in devices:
        print a_device
        show_version(a_device)
        
    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)
if __name__ == "__main__":
    main()

