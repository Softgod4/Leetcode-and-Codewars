import secrets
import string

class passwordgenerate:
    def __init__(self, specialsymbol, numbers, register):
        self.specialsymbol = False
        self.numbers = numbers
        self.register = register
        
    # Библиотека которая генерирует пароли 👇   
    def passwordgenerate(self) -> str:
        password = []
        characters = string.ascii_letters + string.digits
        if self.specialsymbol:
            characters += string.punctuation # добавить специальные символы
        if self.register:
            characters += string.ascii_uppercase # добавить верхний регистр
        for i in range(self.numbers):
            password.append(secrets.choice(characters)) # добавляем случайный символ N раз
        return ''.join(password)
        
    # Тут у меня вопросы для того чтобы сгенерировать правильный пароль 👇     
    def questions(self) -> str:
        symbolsquest = input('Нужны ли спец-символы в пароле? [y\\n]: ')
        if symbolsquest.lower() != 'y' and symbolsquest.lower() != 'n':
            print('Неправильный ввод!')
            return self.questions()
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
                return self.questions()
        except ValueError:
            print('Введите числа от 1 до 100!')
            return self.questions()
        
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
        self.passwordgenerate()
         
if __name__ == '__main__':
    passwd = passwordgenerate(False, 0, False)
    passwd.questions()
    print(f'Ваш пароль: {passwd.passwordgenerate()}')