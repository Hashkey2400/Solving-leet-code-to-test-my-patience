class Solution(object):
    def isPalindrome(self, s):
        """
        Check if a string is a palindrome after removing non-alphanumeric characters
        and converting to lowercase.
        
        Args:
            s: Input string to check
            
        Returns:
            True if the string is a palindrome, False otherwise
        """
        # Filter alphanumeric characters and convert to lowercase
        filtered = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the filtered string reads the same forwards and backwards
        return filtered == filtered[::-1]


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    print('Input: "{}"'.format(s1))
    print("Output: {}".format(solution.isPalindrome(s1)))
    print()
    
    # Example 2
    s2 = "race a car"
    print('Input: "{}"'.format(s2))
    print("Output: {}".format(solution.isPalindrome(s2)))
    print()
    
    # Example 3
    s3 = " "
    print('Input: "{}"'.format(s3))
    print("Output: {}".format(solution.isPalindrome(s3)))
    print()
    
    # Additional test
    s4 = "0P"
    print('Input: "{}"'.format(s4))
    print("Output: {}".format(solution.isPalindrome(s4)))