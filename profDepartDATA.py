import json

#THANK YOU REECE! # thanks Jasper!!
# open a local json file named name_department.json
# IMPORTANT!!!! Make sure it's in the same directory as this .py file

with open('name_department.json') as json_data:
    d = json.load(json_data)

dataD = []
dict = {}

for i in d:
    dict = {}
    p_data = i['data'].split(',')
    dict["Department"] = p_data[3]
    dict["Professor"] = p_data[0] + "," + p_data[1]
    dataD.append(dict)
    
