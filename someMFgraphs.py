import matplotlib.pyplot as plt
from commonProf import departmentRate
from collections import defaultdict
import numpy

def histogramify(data,bins):
	M = max(data)
	m = min(data)
	interval = (M-m)/bins
	hist = defaultdict(int)
	for d in data:
		for i in range(bins):
			if d>m+i*interval:
				f=m+i*interval
		hist[f]+=1
	return hist

intBio = []
for i in departmentRate['bio']:
    intBio.append(int(i))
intEng = []
for i in departmentRate['engineering']:
    intEng.append(int(i))
intPhys = []
for i in departmentRate['physical']:
    intPhys.append(int(i))
intArts = []
for i in departmentRate['Art/Hum/SS']:
    intArts.append(int(i))


countsBio = [ 0 , 0 , 0 , 0 , 0 ]
trash = []
for i in intBio:
    if i == 1:
        countsBio[0] += 1
    elif i == 2:
        countsBio[1] += 1
    elif i == 3:
        countsBio[2] += 1
    elif i == 4:
        countsBio[3] += 1
    elif i == 5:
        countsBio[4] += 1
    else:
        trash.append(i)
        
hist_bio = histogramify(intBio,5)
hist_eng = histogramify(intEng,5)
hist_phys = histogramify(intPhys,5)
hist_arts = histogramify(intArts,5)

xs = range(1,5)

ys = [hist_bio[x] for x in xs]

plt.bar(xs,ys)
