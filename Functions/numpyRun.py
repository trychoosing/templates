import numpy as np

#def myfunc2(*args, **kwargs):
#   for a in args:
#       print a
#   for k,v in kwargs.iteritems():
#       print "%s = %s" % (k, v)

def calculatingBasicNumbers(*args, **kwargs): 
    cal= []
    for a in args:
        print(a)
        cal.append(a)

    for k,v in kwargs.items():
        print(  "%s = %s" % (k, v))
        
        cal.append("%s = %s" % (k, v) )
    return cal