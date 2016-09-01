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
#make rates into Integers
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

#list using floats
fltBio = departmentRate['bio']
fltEng = departmentRate['engineering']
fltPhys = departmentRate['physical']
fltArts = departmentRate['Art/Hum/SS']

#using more increments!! floats by .5
countsBio = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
trash = []
for i in fltBio:
    if i <= 1.5:
        countsBio[0] += 1
    elif i <= 2.0 and i > 1.5:
        countsBio[1] += 1
    elif i <= 2.5 and i > 2.0:
        countsBio[2] += 1
    elif i <=3.0 and i > 2.5:
        countsBio[3] += 1
    elif i <= 3.5 and i > 3.0:
        countsBio[4] += 1
    elif i <= 4.0 and i > 3.5:
        countsBio[5] += 1     
    elif i <= 4.5 and i > 4.0:
        countsBio[6] += 1
    elif i <= 5.0 and i > 4.5:
        countsBio[7] += 1       
    else:
        trash.append(i)

countsEng = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
trash = []
for i in fltEng:
    if i <= 1.5:
        countsEng[0] += 1
    elif i <= 2.0 and i > 1.5:
        countsEng[1] += 1
    elif i <= 2.5 and i > 2.0:
        countsEng[2] += 1
    elif i <=3.0 and i > 2.5:
        countsEng[3] += 1
    elif i <= 3.5 and i > 3.0:
        countsEng[4] += 1
    elif i <= 4.0 and i > 3.5:
        countsEng[5] += 1     
    elif i <= 4.5 and i > 4.0:
        countsEng[6] += 1
    elif i <= 5.0 and i > 4.5:
        countsEng[7] += 1    
    else:
        trash.append(i)

countsPhys = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
trash = []
for i in fltPhys:
    if i <= 1.5:
        countsPhys[0] += 1
    elif i <= 2.0 and i > 1.5:
        countsPhys[1] += 1
    elif i <= 2.5 and i > 2.0:
        countsPhys[2] += 1
    elif i <=3.0 and i > 2.5:
        countsPhys[3] += 1
    elif i <= 3.5 and i > 3.0:
        countsPhys[4] += 1
    elif i <= 4.0 and i > 3.5:
        countsPhys[5] += 1     
    elif i <= 4.5 and i > 4.0:
        countsPhys[6] += 1
    elif i <= 5.0 and i > 4.5:
        countsPhys[7] += 1    
    else:
        trash.append(i)

countsArts = [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
trash = []
for i in fltArts:
    if i <= 1.5:
        countsArts[0] += 1
    elif i <= 2.0 and i > 1.5:
        countsArts[1] += 1
    elif i <= 2.5 and i > 2.0:
        countsArts[2] += 1
    elif i <=3.0 and i > 2.5:
        countsArts[3] += 1
    elif i <= 3.5 and i > 3.0:
        countsArts[4] += 1
    elif i <= 4.0 and i > 3.5:
        countsArts[5] += 1     
    elif i <= 4.5 and i > 4.0:
        countsArts[6] += 1
    elif i <= 5.0 and i > 4.5:
        countsArts[7] += 1    
    else:
        trash.append(i)

#list number of each review [1, 2, 3, 4, 5] MAKE THIS INCREMENT BY .5 INSTEAD OF 1

countsBioInt = [ 0 , 0 , 0 , 0 , 0 ]
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
        
countsEngInt = [ 0 , 0 , 0 , 0 , 0 ]
trash = []
for i in intEng:
    if i == 1:
        countsEng[0] += 1
    elif i == 2:
        countsEng[1] += 1
    elif i == 3:
        countsEng[2] += 1
    elif i == 4:
        countsEng[3] += 1
    elif i == 5:
        countsEng[4] += 1
    else:
        trash.append(i)

countsPhysInt = [ 0 , 0 , 0 , 0 , 0 ]
trash = []
for i in intPhys:
    if i == 1:
        countsPhys[0] += 1
    elif i == 2:
        countsPhys[1] += 1
    elif i == 3:
        countsPhys[2] += 1
    elif i == 4:
        countsPhys[3] += 1
    elif i == 5:
        countsPhys[4] += 1
    else:
        trash.append(i)

countsArtsInt = [ 0 , 0 , 0 , 0 , 0 ]
trash = []
for i in intArts:
    if i == 1:
        countsArts[0] += 1
    elif i == 2:
        countsArts[1] += 1
    elif i == 3:
        countsArts[2] += 1
    elif i == 4:
        countsArts[3] += 1
    elif i == 5:
        countsArts[4] += 1
    else:
        trash.append(i)

#tbh idrk what this does
hist_bio = histogramify(fltBio,8)
hist_eng = histogramify(fltEng,8)
hist_phys = histogramify(fltPhys,8)
hist_arts = histogramify(fltArts,8)

#makes the graphs after calling plot.show() but only makes the last graph...
plt.subplot(221)
xs = range(0,8)
ys = [countsPhys[x] for x in xs]
plt.bar(xs,ys)
plt.ylabel('number of reviews')
plt.xlabel('reviews')
plt.title('Phys')

plt.subplot(222)
xs = range(0,8)
ys = [countsArts[x] for x in xs]
plt.bar(xs,ys)
plt.ylabel('number of reviews')
plt.xlabel('reviews')
plt.title('Art')

plt.subplot(223)
xs = range(0,8)
ys = [countsEng[x] for x in xs]
plt.bar(xs,ys)
plt.ylabel('number of reviews')
plt.xlabel('reviews')
plt.title('Engineering')

plt.subplot(224)
xs = range(0,8)
ys = [countsBio[x] for x in xs]
plt.bar(xs,ys)
plt.ylabel('number of reviews')
plt.xlabel('reviews')
plt.title('Bio')


