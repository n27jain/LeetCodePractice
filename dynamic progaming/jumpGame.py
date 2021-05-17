#https://leetcode.com/problems/jump-game/

# works but takes too long
class Solution(object):
    def canJump(self, nums):
        self.hashMap = {}
        return self.canJumpLoop(nums, 0)
        

    def canJumpLoop(self, nums, pos):
        if(pos in self.hashMap):
            return self.hashMap[pos]
        if(pos == (len(nums)-1)):
            return True
        number = nums[pos]
  
        if number == 0: return False
        for i in range(pos+1, 1+pos+number):
            if(i < len(nums)):
                if(self.canJumpLoop(nums, i)):
                    self.hashMap[pos] = True
                    return True
        self.hashMap[pos] = False
        return False  
        

#better solution would be find the location of all of the 0's in the list
# then traverse your way backwards making sure that the previous value is not 1

#Tabulation


import numpy 
# Tabulation
class Solution(object):
    def canJump(self, nums):
        array = numpy.zeros(len(nums), dtype=bool)
        array[0] = True
        
        for i in range(len(array)):
            # print("i:", i, "nums[i]:", nums[i])
            if(nums[i]):
                for j in range(i+1, nums[i]+ i +1):
                    if j >= len(nums):
                        break
                    array[j] = True
            # print(array)
        return array[-1]

