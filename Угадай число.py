# шаг 1. Загадать случайное число +
import random
number = random.randint(1, 100) # Компьютер загадал число
#print(number)
user_number = None #Переменная для числа пользователя
count = 0          #Счетчик уровня сложности пользователя
levels = {1: 10, 2: 5, 3: 3} # Словарь уровней сложности

level = int(input('Введите уровень сложности: На 1 уровне - 10 попыток, '
                  'на 2 уровне - 5 попыток, '
                  'на 3 уровне - 3 попытки ')) #Пользователь вводит уровень сложности
print(f'Вы выбрали {level} уровень сложности')
max_count = levels[level]                      # Поиск поключу в словаре
user_count = int(input('Введите количество пользователей: '))
users = []                  # Список введенных пользователей
for i in range(user_count):     # Цикл для перебора пользователей
    user_name = input('Введите имя пользователя')
    users.append(user_name)     # Функция для добавления пользователя в словарь Users []
    #print(users)
is_winner = False               # Переменная для " если пользователь еще нет
winner_name = None
while not is_winner:            # Цикл будет до тех пор пока пользователь не найден.

    count += 1                   # На 1 каждыйцикл будет прибавлятся счетчик попыток
    if count > max_count:        # если кол-во попыток превышено все проиграли
        print('Все пользователи проиграли')
        break                    # Цикл сразу завершится
    print(f'Попытка № {count}')
    for user in users:           # Здесь цикл перебора для нового пользователя, каждый делает ход
        print(f'Ход пользователя {user} ')
        # Шаг 2. Предложить юзеру ввести число +
        user_number = int(input('Введите число:'))
        if user_number == number: # Условие: ЕСЛИ число пользователя будет равно числу загаданному, ТО будет найден победитель и игра закончится
                is_winner = True
                winner_name = user
                break               # и цикл остановится
        # Шаг 3. Сравнение двух числе. Сравнение результатов.+
        elif number > user_number:
            print(f'Ваше число меньше загаданного')
        else:
            print(f'Ваше число больше загаданного')
else:
    print(f'Победитель {winner_name}')


