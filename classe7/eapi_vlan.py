#!/usr/bin/env python
'''
Using Arista's pyeapi, we create a script that allows us to
add a VLAN (both the VLAN ID and the VLAN name).
'''
import argparse
import pyeapi

def pyeapi_result(output):
    '''
    Return the 'result' value from the pyeapi output
    '''
    return output[0]['result']['vlans']

def search_vlan(vlans, newvlan):
    '''
    we search for a vlan in a list of vlans.
    '''
    vlan_list = []
    for vlan in vlans.items():
        vlan_list.insert(0, vlan[0])
    result = False
    if newvlan in vlan_list:
        result = True
    return result

def main():
    '''
    Use Arista's eAPI to obtain 'show vlans' from the switch.
    '''
    pynet_sw2 = pyeapi.connect_to("pynet-sw2")
    vlans = pynet_sw2.enable("show vlan")
    vlans = pyeapi_result(vlans)
    parser = argparse.ArgumentParser(' Valn Manipulation')
    parser.add_argument('--name', '--list', nargs='+', action='store', dest='list',
                        help='Add a Vlan')
    parser.add_argument('--remove', action='store', dest='remove',
                        help='Remove a Vlan')
    results = parser.parse_args()

    if results.list != None:
        cmds = ['vlan ' + results.list[1], 'name ' + results.list[0]]
        if  not search_vlan(vlans, results.list[1]):
            pynet_sw2.config(cmds)
            print " vlan {}, name {} was added successfully ".\
format(results.list[1], results.list[0])
        else:
            print " vlan {} already exist ".format(results.list[1])
    if results.remove != None:
        cmds = ['no vlan ' + results.remove]
        if search_vlan(vlans, results.remove):
            pynet_sw2.config(cmds)
            print " vlan {} was removed successfully ".format(results.remove)
        else:
            print " vlan {} is abscent from the Vlan Data base ".format(results.remove)
if __name__ == '__main__':
    main()
