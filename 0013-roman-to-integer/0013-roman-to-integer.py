class Solution:
    def romanToInt(self, s):
        """
        Convert a Roman numeral string to an integer.
        
        Args:
            s: A valid Roman numeral string (1-15 characters)
            
        Returns:
            The integer value of the Roman numeral
        """
        # Map Roman symbols to their values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        n = len(s)
        
        for i in range(n):
            # Get current value
            current_val = roman_values[s[i]]
            
            # If this is not the last character and the next character
            # has a greater value, we need to subtract current value
            if i < n - 1 and current_val < roman_values[s[i + 1]]:
                total -= current_val
            else:
                total += current_val
        
        return total


# Test cases
if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
        ("IV", 4),
        ("IX", 9),
        ("XL", 40),
        ("XC", 90),
        ("CD", 400),
        ("CM", 900),
    ]
    
    print("Testing Roman to Integer Converter:")
    print("-" * 40)
    for roman, expected in test_cases:
        result = solution.romanToInt(roman)
        status = "✓" if result == expected else "✗"
        print("{} {} -> {} (expected: {})".format(status, roman, result, expected))