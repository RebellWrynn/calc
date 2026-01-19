from randomnum import test1,test2

print("Решите задачу:",test1(), "+", test2())

sum = test1()+test2()
sumtest = int(input())

if sum == sumtest:
    print("верно")
else:
    print("не верно")