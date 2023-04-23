# Реализуйте 3 метода, чтобы в каждом из них получить разные исключения

# в данном примере я реализовал калькулятор

def GetMeaning():
    while True:
        num_1 = Error_Value_from_num_1()
        print(num_1)    
        action = Error_Action()
        print(action)
        num_2 = Error_Value_from_num_2()
        print(num_2)    
        if num_2 == '0' and action == '/' or action == '//' :
            print('Error: Zero\n Нельзя делить на ноль')            #проверка на 1 из ошибок, деление на ноль
        else:
            break
    summ = num_1+action+num_2
    print(summ)
    return(summ)


def Calc(summ):  
    print(eval(summ))


def Main():
    while True:
        Calc(GetMeaning())
        stop = input('Остановить калькулятор?(no/yes) ')
        if stop == 'yes':
                break


def Error_Value_from_num_1():                               #Проверка на то, что пользователь ввёл число 
    while True:
        try:
            num_1 = (input('Введите первое число: '))
            int(num_1)
            return(num_1)
        except:
            print('Error:ValueError\nВведите именно число')


def Error_Value_from_num_2():                               #Проверка на то, что пользователь ввёл число 
    while True:
        try:
            num_2 = (input('Введите второе число: '))
            int(num_2)
            return(num_2)
        except:
            print('Error:ValueError\nВведите именно число')
        

def Error_Action():                                         #Проверка на то, что пользователь ввёл действие над числами
    while True:
        action = (input('Введите действие: '))
        if action == '/' or action == '*' or action == '-' or action == '+' or action == '//' or action == '**' or action == '%':
            return(action)
        else:
            print('Error:InvalidAction\nВведите действие которое хотите совершить с числами')
      
      
if __name__=="__main__":
      Main()