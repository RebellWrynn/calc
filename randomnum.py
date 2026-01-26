from time import time

def test():
    current_time = time()
    a = (current_time / 129) - (current_time // 129)
    b = list(str(a))
    c = b[-3:]
    forint = map(str,c)
    forint1 = ''.join(forint)
    return int(forint1)