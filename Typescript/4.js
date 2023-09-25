function isPalindrome(x) {
    var digits = x.toString().split('').map(Number);
    if (digits == digits.reverse()) {
        return true;
    }
    return false;
}
;
