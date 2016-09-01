from rateMyProf_scraper import profDepartmentList
from rateMyProf_scraper import rateMyProfList

#list of common professors
cmProf = []
no = 0
for i in rateMyProfList:
    for n in profDepartmentList:
        if n[0] in i[0]:
            cmProf.append(n[0])
        else:
            no = no + 1

#clean profDepartmentList
cmProfDepart = []
no = 0
for i in profDepartmentList:
    for n in cmProf:
        if n in i[0]:
            cmProfDepart.append(i)
        else:
            no = no + 1


#clean rateMyProfList
cmProfRate = []
no = 0
for i in rateMyProfList:
    for n in cmProf:
        if n in i[0]:
            cmProfRate.append(i)
        else:
            no = no + 1

''' if cmProfDepart[i][0] == cmProfRate[i][0]
then...
dict[cmProfDepart[i][1]] = [cmProfRate[i][1]]'''

departmentRate = {}
no = 0
for i in cmProfDepart:
    for n in cmProfRate:
        if n[0] == i[0]:
            departmentRate[i[1]] = [n[1]]
        else:
            no = no + 1


dict1 = {1:"one" , 2:"two"}

