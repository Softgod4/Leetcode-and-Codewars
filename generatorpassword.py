import secrets
import string

class passwordgenerate:
    def __init__(self, specialsymbol, numbers, register):
        self.specialsymbol = False
        self.numbers = numbers
        self.register = register
           
    def Passwordgenerate(self) -> str:
        password = []
        characters = string.ascii_letters + string.digits
        if self.specialsymbol:
            characters += string.punctuation # добавить специальные символы
        for i in range(self.numbers):
            password.append(secrets.choice(characters)) # добавляем случайный символ N раз

        if self.register:
            return ''.join(password)
        else:
            return ''.join(password).lower()
        
    # Тут у меня вопросы для того чтобы сгенерировать правильный пароль 👇     
    def Questions(self) -> str:
        symbolsquest = input('Нужны ли спец-символы в пароле? [y\\n]: ')
        if symbolsquest.lower() != 'y' and symbolsquest.lower() != 'n':
            print('Неправильный ввод!')
            return self.Questions()
        elif symbolsquest.lower() == 'n':
            print('Без спец-символов!')
            self.specialsymbol = False
        else:
            self.specialsymbol = True
            print('Выбраны спец-символы')
        
        try:
            numbersquest = int(input('Выберите количество символов в пароле [1/100]: '))
            if numbersquest >= 1 and numbersquest <= 100:
                print(f'В пароле будет {numbersquest}')
                self.numbers = numbersquest
            else:
                print('Введите числа от 1 до 100!')
                return self.Questions()
        except ValueError:
            print('Введите числа от 1 до 100!')
            return self.Questions()
        
        registerquest = input('Нужен ли верхний регистр? [y\\n]: ')
        if registerquest.lower() != 'y' and registerquest.lower() != 'n':
            print('Неправильный ввод')
            return self.questions()
        elif registerquest.lower() == 'n':
            print('Без верхнего регистра')
            self.register = False
        else:
            self.register = True
            print('Выбран верхний регистр')
        
        # Все проверки пройдены начинаем генерировать пароль 👇
        self.Passwordgenerate()
         
if __name__ == '__main__':
    passwd = passwordgenerate(False, 0, False)
    passwd.Questions()
    print(f'Ваш пароль: {passwd.Passwordgenerate()}')