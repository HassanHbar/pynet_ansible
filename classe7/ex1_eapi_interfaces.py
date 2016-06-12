'''
Use Arista's eAPI to obtain 'show interfaces' from the switch.
Parse the 'show interfaces' output to obtain the 'inO    ctets' and
'outOctets' fields for each of the interfaces on the switch.
Accomplish this using Arista's pyeapi.
'''
#!/usr/bin/env python

import pyeapi

def main():
    '''
    Use Arista's eAPI to obtain 'show interfaces' from the switch.
    Parse the 'show interfaces' output to obtain the 'inO    ctets' and
    'outOctets' fields for each of the interfaces on the switch.
    Accomplish this using Arista's pyeapi.
    '''
    pynet_sw2 = pyeapi.connect_to("pynet-sw2")
    show_int = pynet_sw2.enable("show interfaces")
    show_int = show_int[0]
    show_int = show_int['result']
    show_int = show_int['interfaces']
    print "\n{:20} {:<20} {:<20}".format("Interface:", "inOctets", "outOctets")
    for key in show_int:
        if "Vlan" not in key:
            print ('{}\t{}\t{}').format(key, show_int[key]['interfaceCounters']\
['inOctets'], show_int[key]['interfaceCounters']['outOctets'])

if __name__ == "__main__":
    main()
