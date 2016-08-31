#!/usr/bin/env python

"""
Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2
"""
from getpass import getpass
import time
import paramiko

MAX_BUFFER = 65535

def send_command(ssh, cmd=''):
    """
    Send command down the channel and return an output
    """
    cmd = cmd.strip()
    ssh.send(cmd + '\n')
    time.sleep(1)
    return ssh.recv(MAX_BUFFER), cmd

def main():
    """
    Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2
    """
    remote_conn = paramiko.SSHClient()
    remote_conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ip_addr = "184.105.247.71"
    username = "pyclass"
    password = getpass()
    remote_conn.connect(ip_addr, username=username, password=password, allow_agent=False,\
    look_for_keys=False)
    ssh = remote_conn.invoke_shell()
    time.sleep(1)
    send_command(ssh, cmd='conf t')
    send_command(ssh, cmd='logging buffered 32000')
    send_command(ssh, cmd='exit')
    outp = send_command(ssh, cmd="show runn | i logging")
    print "\n"*2
    print "#"*85
    print ''' Outputs of the command "{0}" for device =====> {1} is :'''.format(outp[1], ip_addr)
    print "#"*85
    print
    print outp[0]
    print
    print "#"*85

if __name__ == "__main__":
    main()
