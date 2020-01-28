class Solution:
    '''
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #for each element add to all others in the list
        result = []
        set_list = set(nums)
        for i in range(0,len(nums)):
            srch = target - nums[i]
            if (srch in set_list):
                index = nums.index(srch)
                if index!=i:
                    result.append(i)
                    result.append(index)
                    return result
        i+=1
