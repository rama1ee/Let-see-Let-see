print('\n')
def getElement(variable, text):
    while True:
        try:
            if variable == int:
                value = variable(input(text))
                if value == 0 and text == '100 санына бөлгіш жазыңыз: ':
                    raise ZeroDivisionError
                elif value < 0 and text == 'Оң сан енгізіңіз: ':
                    raise ValueError
                return value
            
            elif variable == 'file':
                file = open('./data.txt', 'r')
                if not file:
                    raise FileNotFoundError
                
        except ValueError:
            if ValueError:
                print('Қате: тек сандарды енгізіңіз!\n')
            elif value < 0:
                print('Қате: тек оң сандарды енгізіңіз!\n')
        except ZeroDivisionError:
            print('Қате: нөлге бөлуге болмайды!\n')
        except FileNotFoundError:
            print('Қате: файл табылмады!\n')
            break
        


def checkValueError():
    print('1. Тапсырма: ')
    num = getElement(int, 'Сан енгізіңіз: ')
    return print(f'Енгізілген саныңыз: {num}\n')

def checkZeroDivisionError():
    print('2. Тапсырма: ')
    num = getElement(int, '100 санына бөлгіш жазыңыз: ')
    return print(f'Енгізілген бөлгіш нәтижесі: {100 / num}\n')

def checkFileNotrFound():
    print('3. Тапсырма: ')
    getElement('file', 'Файл табу процесі атқарылып жатыр')

def checkNegativeValueError():
    print('4. Тапсырма: ')
    num = getElement(int, 'Оң сан енгізіңіз: ')
    return print(f'Енгізілген саныңыз: {num}\n')


checkValueError()
checkZeroDivisionError()
checkFileNotrFound()
checkNegativeValueError()
#ffsf
print('\n')