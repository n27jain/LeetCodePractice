# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Brute Force
class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            check = nums[i]
            j = i + 1
            while(j < len(nums)):
                compare = nums[j]
                if(check + compare == target):
                    return [i,j]
                j += 1
                    
#Hash table

class Solution(object):
    def twoSum(self, nums, target):
        for i in range (len(nums)):
            check = nums[i]
            print(check)
            complementary =  target - check
            print(complementary)
            try:
                find = nums.index(complementary, i+1)
                print(i, find)
                if(find):
                    return i, find
            except :
                pass
        
