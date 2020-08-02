# name = input("what's your name?")
# age = input("how old are you?")
# print(f'{name} is {age}')
# print(name + ' is ' + age)

# name = input("what's our name?")
# year = '1995'
# age = 2020 - int(year) + 1
# print(f'{name} is {age}')

# def ready(money):
#     hamberger = 3000
#     print("this is test1")
#     print("this is second")
#     print("this is third")
#     charge = money - hamberger
#     return charge


# myCharge = ready(5000)
# print(f'남은 돈은 총 {myCharge}원 입니다.')

# my_duple = [1, 2, 3, 4, 5, 6]
# for a in my_duple:
#     print(a)

# name = 'tiger rabbit cat lion'
# my_duple = []
# my_duple = name.split()
# print(my_duple)

import random
students = ['kan', 'ann', 'john', 'tiger', 'adward', 'bill']
print(random.choice(students))
print(random.sample(students, 2))
print(random.sample(range(1, 46), 6))
print(random.randint(8, 10))
