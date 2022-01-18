

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        dict = {}
        
        for i, val in enumerate(nums):
            reVal = target - val
            if (reVal in dict):
                return [dict[reVal], i]
            else:
                dict[val] = i
                #store the current value of iteration if it does not existed in hash
                #hash takes O(1) to find element in the hash