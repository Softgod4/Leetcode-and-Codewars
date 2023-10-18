import math
import random
 
def is_prime() -> int:
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    return random.choice(prime_numbers)

def min() -> int:
    msg = int(input())

    p = is_prime()
    q = is_prime()
    n = p*q
    print(f"n = {p*q}")

    phi = ((p-1)*(q-1))

    e = 4

    while(1<e<phi):
        if (math.gcd(e, phi) == 1): #Возвращает наибольший общий делитель указанных целочисленных аргументов. Если какой-либо из аргументов отличен от нуля, то возвращаемое значение является наибольшим положительным целым числом, которое является делителем всех аргументов.
            break
        else:
            e += 1
 
    print("e =", e)

    k = e
    d = ((k*phi)+1) / e
    print("d =", d)
    print(f'Public key: {e, n}')
    print(f'Private key: {d, n}')
    print(f'Original message:{msg}')
 
    C = pow(msg, e)
    C = math.fmod(C, n)
    print(f'Encrypted message: {C}') #Расшифрованное сообщение
 
    M = pow(C, d)
    M = math.fmod(M, n)
 
    print(f'Decrypted message: {M}') #Зашифрованное сообщение

if __name__ == "__main__":
    min()