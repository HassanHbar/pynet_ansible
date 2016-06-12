#!/usr/bin/env python

"""
    Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2
"""
from getpass import getpass
import time
import paramiko

MAX_BUFFER = 65535

def send_command1(ssh, cmd='ter len 0'):
    """
    Send command down the cahnnel without returning an output such disable output paging, enabling config mode, disable config mode
    """
    cmd = cmd.strip()
    ssh.send(cmd + '\n')
    time.sleep(1)
 
def send_command2(ssh, cmd=''):
    """
    Send command down the channel and return an output
    """
    cmd = cmd.strip()
    ssh.send(cmd + '\n')
    time.sleep(1)
    return ssh.recv(MAX_BUFFER)

def main():
    """
    Use Paramiko to change the 'logging buffered <size>' configuration on pynet-rtr2
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
    send_command1(ssh)
    send_command1(ssh, cmd='conf t')
    send_command1(ssh, cmd='logging buffered 32000')
    send_command1(ssh, cmd='exit')
    outp = send_command2(ssh, cmd="show runn | i logging")
    print outp

if __name__ == "__main__":
    main()
