from randomnum import test

# генерация задачи
def gener_task():
    
    a = test()

    b = test()

    num_sum = a + b

    return a,b,num_sum

# ответ
def user_answer():
    user_answer = int(input())
    return user_answer

# сравнение ответа пользователя с решением
def comparison(def_user_answer, num_sum):

    if def_user_answer == num_sum:
        print("верно")
    else:
        print("неверно")





a,b,num_sum = gener_task()

print(f"Решите задачу: {a} + {b}")

x = user_answer()

comparison(x,num_sum)

