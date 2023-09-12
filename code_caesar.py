class Cipher:
    def __init__(self, code, shift):
        self.code = code
        self.shift = shift

    # Выполнение шифра цезаря (работает не в одну сторону, можно ввести 33 и получиться А) 👇
    def coddingcode(self) -> str:
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        arraycode = list(self.code)
        shifr = []
        
        # Ужасное название сори, кстати он проверяет на англ символы 👇
        for i in range(len(arraycode)):
            try:
                gaf = alphabet.index(arraycode[i].lower())
                gaf += self.shift
                shifr.append(alphabet[gaf])
            except:
                print('нужно вводить только русский текст.')
                self.transcript()
                
        return (''.join(shifr))
    
    # Функция для ввода всех значений (сделал отдельно специально) 👇
    def transcript(self) -> str:
        self.code = input('Введите текст для шифрования: ')
        try:
            self.shift = int(input('Введите на сколько чисел сделать сдвиг (только числа): '))
            if self.shift >= 32:
                print('нельзя сделать такой большой сдвиг')
                self.transcript()
        except:
            print('только числа!')
            self.transcript()
        self.coddingcode()

if __name__ == '__main__':
    cipher = Cipher("", 0)
    cipher.transcript()
    result = cipher.coddingcode()
    print("Зашифрованный текст:", result)
