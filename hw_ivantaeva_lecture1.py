import random 

def search_number_in_array(target, array):
    if target in array:
        return f"Число {target} найдено в массиве."
    else:
        return f"Число {target} не найдено в массиве."

#Создаю случайный массив чисел от 1 до 100
random_array = [random.randint(1,100) for _ in range(40)]
print("Сгенерированный массив:", random_array)

#Загаданное число
target_number = int(input("Введите число, которое нужно найти среди элементов массива: "))

#Поиск числа в массиве 
result = search_number_in_array(target_number, random_array)
print(result)