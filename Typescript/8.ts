export const digitalRoot = (n: number): number => {
    let arraynum: number[] = n.toString().split('').map(Number);
    
    while (arraynum.length > 1) {
      arraynum = arraynum.reduce((accumulator, currentValue) => accumulator + currentValue)
        .toString()
        .split('')
        .map(Number);
    }
    
    return arraynum[0];
  };
console.log(digitalRoot(16));
