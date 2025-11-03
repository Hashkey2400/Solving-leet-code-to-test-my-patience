# COPY THIS ENTIRE CODE TO LEETCODE (Replace everything in the editor)

class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        
        return k


# Test locally (LeetCode will ignore this part)
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [1, 1, 2]
    k1 = sol.removeDuplicates(nums1)
    print("Example 1: k =", k1, ", nums =", nums1[:k1])
    
    # Example 2
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k2 = sol.removeDuplicates(nums2)
    print("Example 2: k =", k2, ", nums =", nums2[:k2])