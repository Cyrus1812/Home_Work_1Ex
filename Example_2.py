# Реализуйте метод, принимающий в качестве аргументов два целочисленных массива,
#  и возвращающий новый массив, каждый элемент которого равен разности элементов двух входящих массивов в той же ячейке. 
#  Если длины массивов не равны, необходимо как-то оповестить пользователя.

def Main():
    data = GetMassivs()
    result = Difference(data[0],data[1],data[2])
    print(f'Первый массив = {data[0]}\nВторой массив = {data[1]}\nРезультирующий массив = {result}')
    

def GetMassivs():
    mass_1,mass_2 = [1,5,9,23,43],[7,3,14,6,33]  # для проверки работоспособности можно убрать\добавить несколько чисел в любом из массивов
    if len(mass_1)>len(mass_2):
        lengths = len(mass_2)
        #оповещает пользователя о том что массивы не равны по длинне
        print(f'Первый массив больше второго на {len(mass_1)-len(mass_2)}, выполняю разность до длинны второго массива, а именно: {len(mass_2)}')       
    elif len(mass_2)>len(mass_1):
        #оповещает пользователя о том что массивы не равны по длинне
        print(f'Второй массив больше первого на {len(mass_2)-len(mass_1)}, выполняю разность до длинны первого массива, а именно: {len(mass_1)}')
        lengths = len(mass_1)
    else:
        lengths = len(mass_1)
    return(mass_1,mass_2,lengths)


def Difference(array_1,array_2,length):
    mass_result =[]
    for i in range(length):
        num = array_1[i] - array_2[i]
        mass_result.append(num)
    return(mass_result)


if __name__=="__main__":
      Main()