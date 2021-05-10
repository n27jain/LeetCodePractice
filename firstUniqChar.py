#Question

# Given a string s, return the first non-repeating character in it and return its index. If it does not exist, return -1.

#https://leetcode.com/problems/first-unique-character-in-a-string/

class charWithIndex:
      def __init__(self, char, index):
        self.cahr = char
        self.age = index




class Solution(object):

    

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for i in range(len(s)):
            if(i == 0):
                stack.append(charWithIndex(s[i],i))
            else:
                
            
            

            # for j in range(i+1, len(s)):
            #     checkChar = s[j]
            #     if(checkChar)
