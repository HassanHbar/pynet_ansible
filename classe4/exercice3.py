#!/usr/bin/env python
"""
     Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
"""
from getpass import getpass
import pexpect

def send_command(child, cmd, display='#'):
    """
    send command down in the channel
    """
    child.expect(display)
    cmd = cmd.strip()
    child.sendline(cmd)
    child.expect(display)
    return child.before

def main():
    """Use Pexpect to retrieve the output of 'show ip int brief' from pynet-rtr2
    """
    ip_addr = "50.76.53.27"
    username = "pyclass"
    password = getpass()
    port = 8022
    child = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ip_addr, port))
    send_command(child, password, "assword:")
    # child.expect('assword:')
    # child.sendline(password)
    output = send_command(child, "sh ip int brief")
    print output
    
    
if __name__ == "__main__":
    main()
