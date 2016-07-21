#!/usr/bin/env python
""" Week 8, Exercice 8"""

from netmiko import ConnectHandler
from datetime import datetime
from net_system.models import NetworkDevice, Credentials
import django
from multiprocessing import Process, current_process, Queue

def show_version_queue(a_device, q):
    output_dict = {}
    creds= a_device.credentials
    remote_conn = ConnectHandler(device_type=a_device.device_type,
                                 ip=a_device.ip_address, username=creds.username,
                                 password=creds.password,
                                 port=a_device.port, secret='', verbose=False)
    output = ('#' * 80) + '\n'
    output += remote_conn.send_command_expect("show version") + "\n"
    output += ('#' * 80) + '\n'
    output_dict[a_device.device_name] = output
    q.put(output_dict)

def main():
    """Optional bonus question--use a queue to get the output data back from 
        the child processes in question #7. Print this output data to 
        the screen in the main process"""

    django.setup()
    devices = NetworkDevice.objects.all()
    start_time = datetime.now()
    q = Queue(maxsize=20)
    procs = []
    for a_device in devices:
        
        my_proc = Process(target=show_version_queue, args=(a_device, q))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        a_proc.join()
    
    while not q.empty():
        my_dict = q.get()
        for k,v in my_dict.iteritems():
            print k
            print v
    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)
if __name__ == "__main__":
    main()

