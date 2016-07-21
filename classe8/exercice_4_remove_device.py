#!/usr/bin/env python 
"""Class #8, exercise 4"""

import django
from net_system.models import NetworkDevice, Credentials

def main():
    """Remove the two objects created in the previous exercise from the database"""
    django.setup()
    try:
        test1 = NetworkDevice.objects.get(device_name='pynet-test-rtr1')    
        test2 = NetworkDevice.objects.get(device_name='pynet-test-sw5')
        test1.delete()
        test2.delete()
    except NetworkDevice.DoesNotExist:
        pass 
    
    devices = NetworkDevice.objects.all()
    for a_device in devices:
        print a_device, a_device.credentials, a_device.ip_address, a_device.vendor

if __name__ == "__main__":
    main()

