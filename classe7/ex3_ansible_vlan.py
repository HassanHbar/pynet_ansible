#!/usr/bin/env python
'''
Challenge exercise (optional) -- Using Arista's eAPI, write an Ansible module
that adds a VLAN (both a VLAN ID and a VLAN name).  Do this in an idempotent
manner i.e. only add the VLAN if it doesn't exist; only change the VLAN name
if it is not correct.
To simplify this process, use the .eapi.conf file to store the connection
arguments (username, password, host, port, transport).
'''

import pyeapi
from ansible.module_utils.basic import *

def configure(eapi_conn, vlanid, vname=None):
    '''
    Add the given vlan_id to the switch
    Set the vlan_name (if provided)
    '''
    command_str1 = 'vlan {}'.format(vlanid)
    command = [command_str1]
    command_str2 = 'name {}'.format(vname)
    command.append(command_str2)
    eapi_conn.config(command)

def vlan_manipulation(vlans, vlanid, vname):
    '''
    extract data for Vlan manipulation and return:
    0: to not update config
    1: to update Vlan name
    2: to add new vlan
    '''
    data_stats = {}
    vlan_table = []
    for vlan, name in vlans.items():
        vlan_name = name.get('name', {})
        data_stats[vlan] = vlan_name
        vlan_table.append(vlan)
    if vlanid in vlan_table:
        if data_stats[vlanid] == vname:
            return 0
        else:
            return 1
    else:
        return 2

def main():
    '''
    Ansible module to manipulate an Arista VLAN
    '''

    module = AnsibleModule(
        argument_spec=dict(
            switch=dict(required=True),
            vlanid=dict(required=True),
            name=dict(required=False),
        )
    )

    vlan_id = module.params.get('vlanid')
    vlan_name = module.params.get('name')
    switch = module.params.get('switch')
    eapi_conn = pyeapi.connect_to(switch)
    vlans = eapi_conn.enable("show vlan")
    vlans = vlans[0]
    vlans = vlans['result']
    vlans = vlans['vlans']
    if  vlan_manipulation(vlans, vlan_id, vlan_name) != 0:
        configure(eapi_conn, vlan_id, vlan_name)
        if vlan_manipulation(vlans, vlan_id, vlan_name) == 1:
            module.exit_json(msg="VLAN already exists, setting VLAN name", changed=True)
        if vlan_manipulation(vlans, vlan_id, vlan_name) == 2:
            module.exit_json(msg="Adding VLAN including vlan_name (if present)", changed=True)
    else:
        module.exit_json(msg="VLAN already exists, no action required", changed=False)
if __name__ == '__main__':
    main()
