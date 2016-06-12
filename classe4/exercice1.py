#!/usr/bin/env python

"""
    Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2
"""
from getpass import getpass
import time
import paramiko

MAX_BUFFER = 65535

def disable_paging(ssh, cmd='ter len 0'):
    """
    Disable output paging
    """
    cmd = cmd.strip()
    ssh.send(cmd + '\n')
    time.sleep(1)
 
def send_command(ssh, cmd=''):
    """
    Send command down the channel
    """
    cmd = cmd.strip()
    ssh.send(cmd + '\n')
    time.sleep(1)
    return ssh.recv(MAX_BUFFER)

def main():
    """
    Use Paramiko to retrieve the entire 'show version' output from pynet-rtr2
    """
    remote_conn = paramiko.SSHClient()
    remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip_addr = "50.76.53.27"
    username = "pyclass"
    password = getpass()
    port = 8022
    remote_conn.connect(ip_addr, username=username, password=password, allow_agent=False, look_for_keys=False, port=port)
    ssh = remote_conn.invoke_shell()
    time.sleep(1)
    disable_paging(ssh)
    outp = send_command(ssh, cmd="show version")
    print outp

if __name__ == "__main__":
    main()
