# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
# result_list.insert(pos, el)

count = int(input('Введите количество цифр, которое хотите ввести далее'))

i = count
my_list = []

while i > 0:

    digit = input("Введите следующее число".format(i))
    my_list.append(digit)
    print(my_list)
    i -= 1
    a = my_list
    new_list = list(my_list)
    print(new_list)
for i in range(len(new_list)):
     a[i] = a[i]




















#for i in range(len(my_list)):
    #a[i] = a[i]
    #print(my_list)















