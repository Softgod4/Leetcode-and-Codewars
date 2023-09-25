export class Kata {
    static dnaStrand(dna: string): string {
        let array: string[] = []
        for(let i:number = 0; i<dna.length; i++){
            switch(dna[i]) {
                case 'T':  
                    array.push('A')
                    break;
                case 'A':
                    array.push('T')
                    break;
                case 'C':
                    array.push('G')
                    break;
                case 'G':
                    array.push('C')
                    break;
                default:
                    array.push(dna[i])
                    break;
            }
        }
        return array.join('')
    }
}

