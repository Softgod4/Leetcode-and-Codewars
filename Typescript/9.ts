export function rot13(str: string): string {
    let resultString: string[] = []
    const splittedStr = str.split('')
    const deafultAlphabet: string[] = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890.,!?@[`{^<>/:()\' '.split('');
    const rot13Alphabet: string[] = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm1234567890.,!?@[`{^<>/:()\' '.split('');
    for (let i = 0; i<splittedStr.length; i++) {
        let indexWord = rot13Alphabet.indexOf(splittedStr[i])
        resultString.push(deafultAlphabet[indexWord])
    }
    return resultString.join('');
}

console.log(rot13('EBG13 rknzcyr.'))