import urllib
import re
def parseData(fname):
    for l in urllib.urlopen(fname):
        yield l

print "Reading Data..."
gen = parseData('http://www.ratemyprofessors.com/search.jsp?queryBy=schoolId&schoolName=University+of+California+San+Diego&schoolID=1079&queryoption=TEACHER')
data = []
for i in range(1000):
    my_line = gen.next()
    if "class=\"name\"" in my_line: #CHANGE WHATS IN THE QUOTES. IT LOOKS FOR THAT
        print my_line
        for i in range(10):
            print gen.next()
    else:
        data.append(my_line)
print "done"

