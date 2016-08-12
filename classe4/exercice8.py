#!/usr/bin/env python
'''
Use Netmiko to change the logging buffer size and to disable console logging
from a file for both pynet-rtr1 and pynet-rtr2
logging buffered <size>
no logging console
'''

from netmiko import ConnectHandler
from datetime import datetime

pynet1 = {
    'device_type': 'cisco_ios',
    'username': 'pyclass',
    'ip': '184.105.247.70',
    'password': '88newclass',
    'verbose': 'False'
}

pynet2 = {
    'device_type': 'cisco_ios',
    'username': 'pyclass',
    'secret': '',
    'ip': '184.105.247.71',
    'password': '88newclass',
    'verbose': 'False'
}

def main():
    '''
    Use Netmiko to change the logging buffer size and to disable console logging
    from a file for both pynet-rtr1 and pynet-rtr2
    '''

    start_time = datetime.now()

    for a_device in (pynet1, pynet2):
        net_connect = ConnectHandler(**a_device)
        print
        print "Device: {} ========> {}".format(net_connect.find_prompt(),\
        net_connect.ip)
        output = net_connect.send_command("show run | inc logging")
        print
        print "Configuration of {} before applying the file Config is :".\
        format(net_connect.find_prompt())
        print output
        print
        print '*'*80
        net_connect.send_config_from_file(config_file='config_file.txt')
        output = net_connect.send_command("show run | inc logging")
        print "Configuration of {} after applying the file Config is: ".\
        format(net_connect.find_prompt())
        print
        print output
        print '='*80
        print '='*80
    print "\n"*2
    elapsed_time = datetime.now() - start_time
    print "Elapsed time :   {}".format(elapsed_time)
    print "\n"*2
    
if __name__ == "__main__":
    main()
