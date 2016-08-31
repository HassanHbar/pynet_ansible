#!/usr/bin/env python
"""
Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
"""
from getpass import getpass
import pexpect
import time
def send_command(child, cmd):
    """
    send command down in the channel
    """
    child.sendline("\n")
    time.sleep(1)
    child.expect("#")
    cmd = cmd.strip()
    child.sendline(cmd)
    time.sleep(1)
    child.sendline("\n")
    time.sleep(1)
    child.expect('#')
    return child.before + child.after

def main():
    """Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
    """
    ip_addr = "184.105.247.71"
    username = "pyclass"
    password = getpass()
    child = pexpect.spawn('ssh -l {} {}'.format(username, ip_addr))
    child.expect("word:")
    child.sendline(password)
    output = send_command(child, "sh ver")
    print output
    
    
if __name__ == "__main__":
    main()
