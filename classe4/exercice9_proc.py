#!/usr/bin/env python
"""
Bonus Question - Redo exercise6 but have the SSH connections
happen concurrently using either threads or processes.
"""
from multiprocessing import Process, Queue
from datetime import datetime
from netmiko import ConnectHandler

PYNET1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': '88newclass',
    }

PYNET2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': '88newclass',
    }

JUNIPER_SRX = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': '88newclass',
    'secret': '',
    }

def print_output(device, mp_queue, command="show ver"):
    '''
    it execute a command in Netmiko and print out the result
    '''
    pynet_rtr = ConnectHandler(**device)
    output = pynet_rtr.send_command(command)
    to_display = "\n Device: {} ========> {} \n".format(pynet_rtr.find_prompt(),\
    pynet_rtr.ip)
    to_display += output
    to_display += '*'*80 +"\n"*2
    mp_queue.put(to_display)

def main():
    """
    Use Netmiko to execute 'show arp' on pynet-rtr1, pynet-rtr2, and juniper-srx.
    """
    start_time = datetime.now()
    mp_queue = Queue(maxsize=20)
    procs = []

    for device in (PYNET1, PYNET2, JUNIPER_SRX):
        my_proc = Process(target=print_output, args=(device, mp_queue, "show arp"))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        a_proc.join()

    while not mp_queue.empty():
        my_dict = mp_queue.get()
        print my_dict

    print "\n"*2 + "#"*80

    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)

    print "\n"*2 + "#"*80

if __name__ == "__main__":
    main()



