from time import time

#def randomnum ():

#return(a)
def test1():
    a = (time() / 129) - (time() // 129)
    b = list(str(a))
    c = b[-3:]
    forint = map(str,c)
    forint1 = ''.join(forint)
    return forint1

def test2():
    d = (time() / 129) - (time() // 129)
    e = list(str(d))
    f = e[-3:]
    forint2 = map(str,f)
    forint3 = ''.join(forint2)
    return forint3