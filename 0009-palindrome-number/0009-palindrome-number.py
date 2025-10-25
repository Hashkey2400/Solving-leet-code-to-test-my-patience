class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        # Numbers ending in 0 (except 0 itself) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        # Reverse half of the number
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
        
        # Check if the number is equal to its reverse
        # For odd length numbers, we can ignore the middle digit
        return x == reversed_half or x == reversed_half // 10