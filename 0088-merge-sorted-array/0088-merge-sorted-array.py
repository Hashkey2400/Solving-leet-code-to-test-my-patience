class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Merge nums2 into nums1 in-place.
        
        Args:
            nums1: List with length m+n, first m elements are valid
            m: Number of valid elements in nums1
            nums2: List with length n
            n: Number of elements in nums2
        
        Do not return anything, modify nums1 in-place instead.
        """
        # Start from the end of both arrays
        p1 = m - 1  # Pointer for nums1's valid elements
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the final position in nums1
        
        # Merge from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are remaining elements in nums2, copy them
        # (If nums1 has remaining elements, they're already in place)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# Test cases
def test_merge():
    solution = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution.merge(nums1, 3, nums2, 3)
    print("Example 1: " + str(nums1))
    assert nums1 == [1, 2, 2, 3, 5, 6], "Example 1 failed"
    
    # Example 2
    nums1 = [1]
    nums2 = []
    solution.merge(nums1, 1, nums2, 0)
    print("Example 2: " + str(nums1))
    assert nums1 == [1], "Example 2 failed"
    
    # Example 3
    nums1 = [0]
    nums2 = [1]
    solution.merge(nums1, 0, nums2, 1)
    print("Example 3: " + str(nums1))
    assert nums1 == [1], "Example 3 failed"
    
    # Additional test case
    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    solution.merge(nums1, 3, nums2, 3)
    print("Additional test: " + str(nums1))
    assert nums1 == [1, 2, 3, 4, 5, 6], "Additional test failed"
    
    print("\nAll tests passed!")


if __name__ == "__main__":
    test_merge()