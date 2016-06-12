



import json
import yaml



with open("Json-Exercice.json") as f:
    new_list = json.load(f)
print new_list


with open("Yaml_R_Exercice.yml") as f:
    new_list = yaml.load(f)
print new_list

