class Solution(object):
    def twoSum(self, nums, target):
        num_to_store ={}
        for i, num in enumerate(nums):
            numdiff = target - num
            if numdiff in num_to_store:
                return [num_to_store[numdiff],i]
            num_to_store[num]=i
        return []