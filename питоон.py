import random
values = '1234567890qwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+-='
number = input('how many passwords?'+'\n')
length = input('password length?'+'\n')
number=int(number)
length = int(length)
for x in range(number):
    password = ''
    for _ in range(length):
        password += random.choice(values)
    print(password)