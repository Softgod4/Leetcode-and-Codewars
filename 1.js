function moveZeros(arr) {
  const curret = arr.reduce((acc, curr) => {
    if (curr === 0) {
      arr.unshift(curr)
    }
  }, 0)
  return curret
}

console.log(moveZeros([1,2,0,1,0,1,0,3,0,1]))