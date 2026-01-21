from randomnum import test

a = test()

b = test()

sum = a+b

print("Решите задачу:",a, "+", b)
sumtest = int(input())

if sum == sumtest:
    print("верно")
else: print("не верно")