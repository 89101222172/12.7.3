number = [int(x)for x in input("Введите любые числа,через пробел) ").split()]
list(number)
array = number
print(array)
while True:
    try:
        element = int(input("Введите любое число) "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Введите одно число: ")
    except ValueError:
        print("Неверный диапазон ")
number.append(element)
print(number)
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)
# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0,len(array) ))