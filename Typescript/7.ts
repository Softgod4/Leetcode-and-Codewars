export function spinWords(words: string): string {
    let returnArray: string[] = [];
    const splitWords: string[] = words.split(' ')
    for(let i:number=0; i<splitWords.length; i++){
        if(splitWords[i].length >= 5){
           let reverseWord = [...splitWords[i]].reverse().join('')
           returnArray.push(reverseWord)
        } else {
            returnArray.push(splitWords[i])
        }
    }
    return returnArray.join(' ')
}

console.log(spinWords("Hey fellow warriors"))