#make list of lists. list has "name" , "rating" or "name", "department"]

from rateMyProfDATA import dataR
from profDepartDATA import dataD


dataRName = []
for i in dataR:
    m = str(i['Text'])
    x = m.split()[:2]
    dataRName.append(x[0] + x[1])

dataRRating = []
for i in dataR:
    dataRRating.append(i['Rating'])

matrix = [dataRName,dataRRating]

rateMyProfList = [] #1676 professors

for i in range(len(dataRName)):
    rateMyProfList.append([row[i] for row in matrix])


dataDName = []
for i in dataD:
    m = i['Professor']
    x = m.split()[:2]
    dataDName.append(x[0] + x[1])

dataDDepartment = []
for i in dataD:
    dataDDepartment.append(i['Department'])

matrix = [dataDName,dataDDepartment]

profDepartmentList = [] #1676 professors

for i in range(len(dataDName)):
    profDepartmentList.append([row[i] for row in matrix])





