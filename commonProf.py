from rateMyProf_scraper import profDepartmentList
from rateMyProf_scraper import rateMyProfList
print"reading??"
yes = 0
no = 0
for i in profDepartmentList:
    
    if i[0] in rateMyProfList:
        yes = yes + 1
    else:
        no = no + 1
print"done??"
print yes
print no
