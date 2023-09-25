type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
        toBe: (expected: any) => {
            return val === expected;
        },
        notToBe: (expected: any) => {
            return val !== expected;
        }
    };
}