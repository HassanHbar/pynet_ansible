#!/usr/bin/env python
'''
Using SNMPv3 create two SVG image files.
The first image file should graph the input and output octets on interface FA4 on pynet-rtr1
every five minutes for an hour.  Use the pygal library to create the SVG graph file. Note,
you should be doing a subtraction here (i.e. the input/output octets transmitted during
this five minute interval). The second SVG graph file should be the same as the first
except graph the unicast packets received and transmitted
'''
import time
from snmp_helper import snmp_get_oid_v3, snmp_extract
import pygal

IP_ADDR1 = "184.105.247.70"
A_USER = 'pysnmp'
MY_KEY = "galileo1"
AUTH_KEY = MY_KEY
ENCRYPT_KEY = MY_KEY
SNMP_USER = (A_USER, AUTH_KEY, ENCRYPT_KEY)
PYNET_RTR1 = (IP_ADDR1, 161)

OID_DICT = {
    'in_octets':    '1.3.6.1.2.1.2.2.1.10.5',
    'out_octets':   '1.3.6.1.2.1.2.2.1.16.5',
    'in_ucast_pkts':    '1.3.6.1.2.1.2.2.1.11.5',
    'out_ucast_pkts':    '1.3.6.1.2.1.2.2.1.17.5',
}

def get_interface_stats(oid):
    '''
    Extract data for an oid request.
    '''
    snmp_data = snmp_get_oid_v3(PYNET_RTR1, SNMP_USER, oid)
    return int(snmp_extract(snmp_data))

def graph_chart(title, line1_label, line2_label, x_label, line1, line2, file):
    '''
    line1 and line2 is for data points.
    '''
    line_chart = pygal.Line(include_x_axis=True)
    line_chart.title = title
    line_chart.x_labels = x_label
    line_chart.add(line1_label, line1)
    line_chart.add(line2_label, line2)
    line_chart.render_to_file(file)

def main():
    '''
    Using SNMPv3 create two SVG image files.

    1) The first image file should graph the input and output octets on interface
    FA4 on pynet-rtr1 every five minutes for an hour.  Use the pygal library to
    create the SVG graph file. Note, you should be doing a subtraction here
    (i.e. the input/output octets transmitted during this five minute interval).

    2) The second SVG graph file should be the same as the first except graph
    the unicast packets received and transmitted.
    '''

    stats = {
        "in_octets": [],
        "out_octets": [],
        "in_ucast_pkts": [],
        "out_ucast_pkts": [],
    }
    for tim in range(0, 60, 5):
        for oid in ("in_octets", "out_octets", "in_ucast_pkts", "out_ucast_pkts"):
            snmp_retrieved_count = get_interface_stats(OID_DICT[oid])
            stats[oid].append(snmp_retrieved_count)
        print " TIME : {0}".format(tim)
        time.sleep(300)
    print stats
    graph_stats = {}
    for key in stats.keys():
        temp = []
        for index in range(0, len(stats[key])-1):
            temp.append(stats[key][index+1] - stats[key][index])
        graph_stats[key] = temp
    print graph_stats

    x_labels = []
    for x_axis in range(5, 60, 5):
        x_labels.append(str(x_axis))
    graph_chart("pynet-rtr1 Fa4 Input/Output Bytes", "In Octets", "Out Octets",\
    x_labels, graph_stats["in_octets"], graph_stats["out_octets"], "pynet-rtr1-octets.svg")
    graph_chart("pynet-rtr1 Fa4 Input/Output Packets", "In Unicast Packets", "Out Unicast Packets",\
    x_labels, graph_stats["in_ucast_pkts"], graph_stats["out_ucast_pkts"], "pynet-rtr1-pkts.svg")

if __name__ == '__main__':
    main()
