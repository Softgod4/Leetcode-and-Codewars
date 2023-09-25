type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    const count = init

    return {
        increment: () => {
            init += 1;
            return init
        }, 
        decrement: () => {
            init -= 1
            return init
        },
        reset: () => {
            return count
        }
    }
};