#!/usr/bin/env python
"""Week 8, exercice 7"""

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process, current_process

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
    """ Repeat exercise #6 except use processes"""

    django.setup()
    devices = NetworkDevice.objects.all()
    start_time = datetime.now()

    procs = []
    for a_device in devices:
        
        my_proc = Process(target=show_version, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        print a_proc
        a_proc.join()
    
    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)
if __name__ == "__main__":
    main()

