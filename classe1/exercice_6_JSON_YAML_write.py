#!/usr/bin/env python


import json
import yaml


my_list = range(9)
my_list.append("YAML Exercice")
my_list.append("Jason Exercice")
my_list.append({})
my_list[-1]['IP Adress'] = "192.168.1.1"
my_list[-1]['Attributes'] = range (5)

with open("Yaml_Exercice.yml", "w") as f:
    f.write( yaml.dump(my_list, default_flow_style=False))


with open("Json-Exercice.json", "w") as g:
    json.dump(my_list,g)



