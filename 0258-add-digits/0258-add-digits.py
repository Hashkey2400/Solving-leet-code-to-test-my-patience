class Solution:
    def addDigits(self, num):
        while num >= 10:
            total = 0
            temp = num
            while temp:
                total += temp % 10
                temp //= 10
            num = total
        return num