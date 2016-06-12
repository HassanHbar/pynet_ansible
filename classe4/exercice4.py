#!/usr/bin/env python
"""
     Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
"""
from getpass import getpass
import time
import pexpect

def send_command(child, cmd):
    """
    send command down in the channel
    """
    cmd = cmd.strip()
    child.sendline(cmd)
    time.sleep(1)
    child.expect('#')
    return child.before + child.after

def main():
    """Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
    """
    ip_addr = "50.76.53.27"
    username = "pyclass"
    password = getpass()
    port = 8022
    child = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    child.expect('assword:')
    child.sendline(password)
    send_command(child, "conf t")
    send_command(child, "logging buffered 32000 ")
    send_command(child, "end")
    send_command(child, "sh runn | in logging")
    output = send_command(child, "\n")
    print output

if __name__ == "__main__":
    main()
