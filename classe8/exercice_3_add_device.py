#!/usr/bin/env python 
"""Class #8, exercise 3"""

import django
from net_system.models import NetworkDevice, Credentials

def main():
    """Create two new test NetworkDevices in the database. Use both direct object creation and the 
       .get_or_create() method to create the devices."""
    django.setup()
    creds = Credentials.objects.all()
    std_creds = creds[0]
    arista_creds = creds[1]
    
    router_test1 = NetworkDevice(
        device_name='pynet-test-rtr1',
        device_type='cisco_ios',
        credentials=std_creds,
        vendor='Cisco',
        ip_address='184.105.247.77',
        port=22,
    )
    router_test1.save()
    sw_test2 = NetworkDevice.objects.get_or_create(
        device_name='pynet-test-sw5',
        device_type='arista_eos',
        vendor='Arista',
        credentials=arista_creds,
        ip_address='184.105.247.78',
        port=22,
    )
    
    
    devices = NetworkDevice.objects.all()
    
    for a_device in devices:
        print a_device, a_device.credentials, a_device.ip_address, a_device.vendor

if __name__ == "__main__":
    main()

