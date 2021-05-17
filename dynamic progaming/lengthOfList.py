#https://leetcode.com/problems/longest-increasing-subsequence/submissions/



class Solution(object):
    def lengthOfLIS(self, nums):
        self.hashmap = {}

        max = 0
        for i in range(len(nums)):
            size = self.recursiveDef(nums, i)
            if size > max: max = size
        return max
    
    
    def recursiveDef(self, nums, i):
        if(i in self.hashmap):
            return self.hashmap[i]
        
        # if(i == len(nums-1)):
        #     hashmap[i] = 1
        #     return 1
        out = 1
        maxi = 0
        current = nums[i]
        for j in range(i+1, len(nums)):
            if(nums[j] > current ):
                getNext = self.recursiveDef( nums, j)
                if(getNext > maxi): 
                    maxi = getNext
        
        self.hashmap[i] = out + maxi
        return out + maxi    