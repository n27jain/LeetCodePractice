# Given an integer array nums, 
# return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

#Hash but at the same time this uses more memory
class Solution(object):
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            num = nums[i]
            try:
                search =  nums.index(num, i+1)
                return True
            except: pass
        return False


#using sort

class Solution(object):
    def containsDuplicate(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            num = nums[i]
            adjacent = nums[i+1]
            if(num == adjacent):
                return True
        return False