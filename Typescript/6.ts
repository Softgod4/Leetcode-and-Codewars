export function reverseWords(str: string): string {
    let returnArray: string[] = []
    let wordArray = str.split(' ');
    for(let i:number=0; i<wordArray.length; i++){
        let curretArray: string = wordArray[i].split('').reverse().join('');
        returnArray.push(curretArray)
    }
    return returnArray.join(' ');
}

console.log(reverseWords('The quick.'))