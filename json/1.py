import json

with open('/Users/anita/Documents/PP2/lab04/json/sample_data.json', 'r') as file:
    data = json.load(file)
    print("""
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")
    first = data["imdata"]
    for i in first:
        if len(i["l1PhysIf"]["attributes"]["dn"]) ==41:
            print(i["l1PhysIf"]["attributes"]["dn"], " "*30, i["l1PhysIf"]["attributes"]["speed"], "", i["l1PhysIf"]["attributes"]["mtu"] )
        else:
            print(i["l1PhysIf"]["attributes"]["dn"], " "*29, i["l1PhysIf"]["attributes"]["speed"], "", i["l1PhysIf"]["attributes"]["mtu"] )