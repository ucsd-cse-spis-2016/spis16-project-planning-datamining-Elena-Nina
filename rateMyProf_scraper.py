from rateMyProfDATA import dataR


rateMyProfDict = {}
#idk how to make this better. try again tomorrow.today? idek
def name(x):
    m = str(dataR[x]['Text'])
    print m.split()[:2]



def rating(x):
    print dataR[x]['Rating']


