'''
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        i=0
        while i < l-1:
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                l-=1
            else:
                i+=1