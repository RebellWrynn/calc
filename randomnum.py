from time import time

def test():
    a = (time() / 129) - (time() // 129)
    b = list(str(a))
    c = b[-3:]
    forint = map(str,c)
    forint1 = ''.join(forint)
    return int(forint1)