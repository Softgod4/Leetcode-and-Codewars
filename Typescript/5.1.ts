export class Kata {
    static dnaStrand(dna: string): string {
        let array: string[] = []
        for(let i:number = 0; i<dna.length; i++){
            if(dna[i] === 'A'){
                array.push('T')
            } else if(dna[i] === 'T') {
                array.push('A')
            } else if(dna[i] === 'G') {
                array.push('C')
            } else if(dna[i] === 'C') {
                array.push('G')
            } else {
                array.push(dna[i])
            }
        }
        return array.join('')
    }
}

