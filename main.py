import random
password_elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
while True:
    password = input("Введите пароль длинною в 7 символов: ")
    if len(password) < 7:
        print("Пароль должен быть длинною в 7 символов")
        continue
    if len(password) > 7:
        print("Пароль должен быть длинною в 7 символов")
        continue
    if len(password) == 7:
        break

password_list = []
password_list.append(password)
random_password = []
while len(random_password) != 7:
    random_element = random.choice(password_elements)
    random_password.append(random_element)

password_list.append(''.join(random_password))

print(password_list)
