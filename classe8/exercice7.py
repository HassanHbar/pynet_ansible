#!/usr/bin/env python
"""Week 8, exercice 7"""

from datetime import datetime
from multiprocessing import Process, current_process
from netmiko import ConnectHandler
from netmiko import NetMikoTimeoutException, NetMikoAuthenticationException
from net_system.models import NetworkDevice, Credentials
import django

def print_output(a_device):
    '''
    Display Output if we connect to the device, if not it displays
    Timeout or Authentication error while connecting to a device
    '''
    output = execute_command(a_device, "show version")
    if output[0]:
        data = "\n" + '#' * 80 + "\n"
        data += '''Outputs of "{0}" command of "{1}" is :\
        '''.format(output[2], a_device)
        data += "\n" + '#' * 80 + "\n"
        data += output[1]
    else:
        data = "\n" + '#' * 80 + "\n"
        data += '''We get the following error"{0}" when we try to access device"\
        "{1}" '''.format(output[1], a_device)
        data += "\n" + '#' * 80 + "\n"
    print data

def execute_command(a_device, command='show logging'):
    '''
    this function permit to connect to a device and execute a command
    "show logging" is the commande by default.
    it return the command, the command outputs and which printing format we will use
    '''
    creds = a_device.credentials
    try:
        remote_conn = ConnectHandler(device_type=a_device.device_type,
                                     ip=a_device.ip_address, username=creds.username,
                                     password=creds.password,
                                     port=a_device.port, secret='')
        output = remote_conn.send_command_expect(command)
        to_print = True
        return to_print, output, command


    except (NetMikoTimeoutException, NetMikoAuthenticationException) as error:
        to_print = False
        return to_print, error

def main():
    """ Repeat exercise #6 except use processes"""

    django.setup()
    devices = NetworkDevice.objects.all()
    start_time = datetime.now()

    procs = []
    for a_device in devices:

        my_proc = Process(target=print_output, args=(a_device,))
        my_proc.start()
        procs.append(my_proc)

    for a_proc in procs:
        a_proc.join()

    elapsed_time = datetime.now() - start_time
    print "\n" + '#' * 80 + "\n"
    print "Elapsed time :   {}".format(elapsed_time)
    print "\n" + '#' * 80 + "\n"
if __name__ == "__main__":
    main()
