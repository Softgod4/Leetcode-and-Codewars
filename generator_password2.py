import secrets
import string
from dataclasses import dataclass

# код переписан Алексеем, спасибо большое за пулл реквест

@dataclass
class PasswordGenerationOptions:
    use_special_symbols: bool
    symbols_count: int
    use_upper_case: bool


def ask_password_generation_options() -> PasswordGenerationOptions:
    ...


def generate_password(options: PasswordGenerationOptions) -> str:
    password = ""
    characters = string.ascii_letters + string.digits

    if options.use_special_symbols:
        characters += string.punctuation  # добавить специальные символы

    for i in range(options.symbols_count):
        password += secrets.choice(characters)  # добавляем случайный символ

    if not options.use_upper_case:
        password = password.lower()

    return password


class PasswordGenerator:
    # Тут у меня вопросы для того чтобы сгенерировать правильный пароль 👇
    def print_questions(self) -> str:
        symbols_quest = input("Нужны ли спец-символы в пароле? [y\\n]: ")
        if symbols_quest.lower() != "y" and symbols_quest.lower() != "n":
            print("Неправильный ввод!")
            return self.print_questions()
        elif symbols_quest.lower() == "n":
            print("Без спец-символов!")
            self.special_symbol = False
        else:
            self.special_symbol = True
            print("Выбраны спец-символы")

        try:
            numbers_quest = int(
                input("Выберите количество символов в пароле [1/100]: ")
            )
            if numbers_quest >= 1 and numbers_quest <= 100:
                print(f"В пароле будет {numbers_quest}")
                self.numbers = numbers_quest
            else:
                print("Введите числа от 1 до 100!")
                return self.print_questions()
        except ValueError:
            print("Введите числа от 1 до 100!")
            return self.print_questions()

        register_quest = input("Нужен ли верхний регистр? [y\\n]: ")
        if register_quest.lower() != "y" and register_quest.lower() != "n":
            print("Неправильный ввод")
            return self.print_questions()
        elif register_quest.lower() == "n":
            print("Без верхнего регистра")
            self.register = False
        else:
            self.register = True
            print("Выбран верхний регистр")
        self.generate_password()


if __name__ == "__main__":
    options = ask_password_generation_options()

    print(f"Ваш пароль: {generate_password(options)}")