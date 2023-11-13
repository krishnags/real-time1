import json
import os
import pprint
import copy

vol_json_path = os.getcwd() + "\\vol_copy.json"
cifs_json_path = os.getcwd() + "\\cifs_share.json"

def read_json_file(file_path):
    with open(file_path) as file:
        data = json.load(file)
        return data

vol_data = read_json_file(vol_json_path) 
cifs_data = read_json_file(cifs_json_path)   

vol_master_data = copy.deepcopy(vol_data['records'])
cifs_master_data = copy.deepcopy(cifs_data['records'])


for v in range(len(vol_master_data)):
    vserver = vol_master_data[v]['vserver']
    volume = vol_master_data[v]['volume']
    print(f"volume: {volume}, vserver: {vserver}")
    for share_dict in cifs_master_data:
        share_list = []
        if vserver == share_dict['vserver'] and volume == share_dict.get('volume'):
            print(f"share: {share_dict['share_name']}")
            #append to the shares_list with , and make it a string
            share_list.append(share_dict['share_name'])
            vol_master_data[v]['shares'] = share_list
            #print(vol_master_data[v]['shares'])
        else:
            continue
    
# print the dictionary if the share key value list length is greater than 1. 
# Handle the NoneType error if the list is empty and key doesnt exist
for v in range(len(vol_master_data)):
    if vol_master_data[v].get('shares'):
        if len(vol_master_data[v]['shares']) > 1:
             print(vol_master_data[v])
        if len(vol_master_data[v]['shares']) == None:
            continue
    else:
        continue        







