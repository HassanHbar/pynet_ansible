


from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("config_file.txt")

crypto= cisco_cfg.find_objects(r"^crypto map CRYPTO")


print "Exercice 8 =========================================="
for i in crypto:
    print i.text



exercice9= cisco_cfg.find_objects_w_child(parentspec= r"^crypto map CRYPTO", childspec=r"set pfs group2")

print "Exercice 9 =========================================="
for i in exercice9:
    print i.text





exercice10= cisco_cfg.find_objects_wo_child(parentspec= r"^crypto map CRYPTO", childspec=r"transform-set AES-SHA")

print "Exercice 10 =========================================="
for i in exercice10:
    print i.text

