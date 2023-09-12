class Cipher:
    def __init__(self, code, shift):
        self.code = code
        self.shift = shift
        
    def coddingcode(self) -> str:
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        arraycode = list(self.code)
        shifr = []
        for i in range(len(arraycode)):
            try:
                gaf = alphabet.index(arraycode[i].lower())
                gaf += self.shift
                shifr.append(alphabet[gaf])
            except:
                print('нужно вводить только русский текст.')
                self.transcript()
                
        return (''.join(shifr))
    
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
        
class passwdecryption:
    def __init__(self, code):
        self.code = code
        
    def transcript(self) -> str:
        alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
        self.code = input('Введите зашифрованный текст: ')

        iteration = 1  
        while True:
            transcriptcode = [] 
            
            for i in range(len(self.code)):
                x = alphabet.index(self.code[i])
                transcriptcode.append(alphabet[x+iteration])

            print(''.join(transcriptcode))
            
            codequiz = input('расшифровано? [y\\n]: ')
            if codequiz.lower() != 'y' and codequiz.lower() != 'n':
                print('Неправильный ввод')
                break
            elif codequiz.lower() == 'n':
                iteration += 1
                continue
            else:
                print('Расшифровано!')
                break

if __name__ == '__main__':
    try:
        quiz = int(input('1 - Расшифровать шифр / 2 - Зашифровать шифр: '))
        if quiz == 1:
            decryption = passwdecryption("")
            decryption.transcript()
            result = decryption.decodingcode()
            print("Расшифрованный текст:", result)
        elif quiz == 2:
            cipher = Cipher("", 0)
            cipher.transcript()
            result = cipher.coddingcode()
            print("Зашифрованный текст:", result)
        else:
            print("Некорректный выбор.")
    except Exception as e:
        print('')