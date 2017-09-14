def read(csv):
    thefile = open(csv, 'r')
    l = thefile.readlines()
    thefile.close()
    return l


def makeDictionary(l):
    
