import urllib
import re
def parseData(fname):
    for l in urllib.urlopen(fname):
        yield l

dataDName = [] #733 professors
gen = parseData('http://www.ucsd.edu/catalog/front/faculty.html')

dataDDepartment = []
trash = []
for i in gen:
    myLine = gen.next()
    if "</strong>" in myLine:
        print myLine
        for i in range(1) and range(2):
            print gen.next()
    else:
        trash.append(myLine)


        

gen = parseData('http://www.ucsd.edu/catalog/front/faculty.html')
for i in gen:
    myLine = gen.next()
    if "<strong>" in myLine:
        a = myLine.find("<strong>")
        b = myLine.find("</strong>")
        m = myLine[a+len("<strong>"):b-1]
        x = m.split()[:2]
        dataDName.append(x[0] + x[1])
        

        
'''
dataD = []
trash = []


for i in gen:
    myLine = gen.next()
    if "<strong>" in myLine:
        print myLine
        for i in range(2):
            print gen.next()
    else:
        trash.append(myLine)
print "done"
'''


