'''
Given an array, rotate the array to the right by k steps, where k is non-negative.
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < k:
            l = len(nums)
            a = nums[l-1]
            nums.insert(0,a)
            nums.pop()
            i += 1
        '''
        Insert last item to beginning of list. Pop last item. Repeat until k
        '''
 
                
        