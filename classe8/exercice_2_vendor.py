#!/usr/bin/env python 
"""Class #8, exercise 2"""

import django
from net_system.models import NetworkDevice, Credentials

def main():
    """Set the vendor field of each NetworkDevice to the appropriate vendor."""
    django.setup()
    devices = NetworkDevice.objects.all()

    for a_device in devices:
        if 'pynet-sw' in a_device.device_name:
            a_device.vendor = 'Arista'
        elif 'pynet-rtr' in a_device.device_name:
            a_device.vendor = 'Cisco'
        elif 'juniper' in a_device.device_name:
            a_device.vendor = 'Juniper'
        a_device.save()

    for a_device in devices:
        print a_device, a_device.vendor

if __name__ == "__main__":
    main()

