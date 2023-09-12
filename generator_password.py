import secrets
import string

class PasswordGenerate:
    def __init__(self, specialsymbol, numbers, register):
        self.special_symbol = False
        self.numbers = numbers
        self.register = register
           
    def password_generate(self) -> str:
        password = []
        characters = string.ascii_letters + string.digits
        if self.special_symbol:
            characters += string.punctuation # добавить специальные символы
        for i in range(self.numbers):
            password.append(secrets.choice(characters)) # добавляем случайный символ N раз

        if self.register:
            return ''.join(password)
        else:
            return ''.join(password).lower()
        
    # Тут у меня вопросы для того чтобы сгенерировать правильный пароль 👇     
    def questions(self) -> str:
        symbols_quest = input('Нужны ли спец-символы в пароле? [y\\n]: ')
        if symbols_quest.lower() != 'y' and symbols_quest.lower() != 'n':
            print('Неправильный ввод!')
            return self.Questions()
        elif symbols_quest.lower() == 'n':
            print('Без спец-символов!')
            self.special_symbol = False
        else:
            self.special_symbol = True
            print('Выбраны спец-символы')
        
        try:
            numbers_quest = int(input('Выберите количество символов в пароле [1/100]: '))
            if numbers_quest >= 1 and numbers_quest <= 100:
                print(f'В пароле будет {numbers_quest}')
                self.numbers = numbers_quest
            else:
                print('Введите числа от 1 до 100!')
                return self.Questions()
        except ValueError:
            print('Введите числа от 1 до 100!')
            return self.Questions()
        
        register_quest = input('Нужен ли верхний регистр? [y\\n]: ')
        if register_quest.lower() != 'y' and register_quest.lower() != 'n':
            print('Неправильный ввод')
            return self.questions()
        elif register_quest.lower() == 'n':
            print('Без верхнего регистра')
            self.register = False
        else:
            self.register = True
            print('Выбран верхний регистр')
        self.password_generate()
         
if __name__ == '__main__':
    passwd = PasswordGenerate(False, 0, False)
    passwd.questions()
    print(f'Ваш пароль: {passwd.password_generate()}')