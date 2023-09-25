function twoSum(nums: number[], target: number): number[] {
    let returnarray: number[] = []
    for(let index:number = 0; index<nums.length; index++){
        for(let indexes:number = 1; indexes<nums.length;indexes++) {
            if(nums[indexes] + nums[indexes+1] === target) {
                return returnarray = [nums[index], nums[indexes]]
            }
        }
    }
    return returnarray
};