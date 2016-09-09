from dataR_D_scraper import profDepartmentList
from dataR_D_scraper import rateMyProfList
from departments import arts_And_HumanitiesSS
from departments import bio
from departments import engineering
from departments import physical
from departments import management
from departments import global_policy
from departments import medicine
from departments import scripps
from departments import pharmacy

#to get this to work, 4 windows must be opened! all from desktop!


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


#turns department into school
other = []
for i in cmProfDepart:
    i[1] = i[1].split()
    for n in i[1]:
        if n in physical:
            i[1] = "physical"
        elif n in bio:
            i[1] = 'bio'
        elif n in engineering:
            i[1] = 'engineering'
        elif n in management:
            i[1] = 'management'
        elif n in global_policy:
            i[1] = 'global policy'
        elif n in medicine:
            i[1] = 'medicine'
        elif n in scripps:
            i[1] = 'scripps'
        elif n in pharmacy:
            i[1] = 'pharmacy'
        elif n in arts_And_HumanitiesSS:
            i[1] = 'Art/Hum/SS'
        else:
            other.append(i[1])


''' if cmProfDepart[i][0] == cmProfRate[i][0]
then...
dict[cmProfDepart[i][1]] = [cmProfRate[i][1]]?????'''
#using physical , Art/Hum/SS , bio , engineering
departmentRate = {}
no = 0
for i in cmProfDepart:
    key = i[1]
    for n in cmProfRate:
        if i[0] == n[0]:
            departmentRate.setdefault(key, [])
            departmentRate[key].append(n[1])
        else:
            no = no + 1



#cmProfDepart[0]
#cmProfRate[0]
#departmentRate['engineering']
