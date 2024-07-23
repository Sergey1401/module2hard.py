# Задание "Слишком древний шифр":
def password(number):
    pass_n = ' '
    for i in range(1, number):
        for j in range(i + 1, number):
            if number % (i + j) == 0:
                pass_n += str(i) + str(j)
    return pass_n


print('Введите число от 3 до 20: ')
print('Пароль: ', password(int(input())))
