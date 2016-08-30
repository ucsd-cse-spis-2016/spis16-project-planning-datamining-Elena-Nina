from rateMyProfDATA import dataR

dataRName = []
for i in dataR:
    m = str(i['Text'])
    x = m.split()[:2]
    dataRName.append(x[0] + x[1])

dataRRating = []
for i in dataR:
    dataRRating.append(i['Rating'])

matrix = [dataRName,dataRRating]

rateMyProfList = []

for i in range(len(dataRName)):
    rateMyProfList.append([row[i] for row in matrix])





