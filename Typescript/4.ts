function isPalindrome(x: number): boolean {
    const digits = x.toString().split('').map(Number);
    if (digits == digits.reverse()) {
        return true
    }
    return false
};

