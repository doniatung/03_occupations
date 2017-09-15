def read(csv):
    thefile = open(csv, 'r')
    l = thefile.readlines()
    thefile.close()
    return l


def makeDictionary(l):
    d = {}
    del l[0]
    del l[-1]
    for x in l:
        if x.count(",") > 1:
            quote = x.find('"', 1, len(x))
            k = x[1 : quote]
            v = float(x[quote + 2: -2])
            d[k] = v
        else:
            comma = x.find(",")
            k = x[: comma]
            v = float(x[comma + 1: -2])
            d[k] = v
    return d 

def pickOne(d):
    
    
    

print makeDictionary(read("occupations.csv"))
    
    
        
