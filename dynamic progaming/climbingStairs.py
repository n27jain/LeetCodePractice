# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# https://leetcode.com/problems/climbing-stairs/


#brute force fib sequence recursion
class Solution(object):
    def climbStairs(self, n):
        if(n<=2):
            return n
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)


#brute force fib sequence for loop and memstorage
class Solution(object):
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n
        first = 1
        second = 2
        for i in range(n-2):
            third =  first + second
            first = second 
            second = third
        return second

#using memoization
class Solution(object):
    def climbStairs(self, n):
        dictionary = {}
        return self.with_memo(n, dictionary)

    def with_memo(self, n, dictionary):

        if(n in dictionary):
            return dictionary[n]
        if(n<= 2):
            dictionary[n] = n
            return n
        else:
            dictionary[n] =  self.with_memo(n-1, dictionary) + self.with_memo(n-2, dictionary)
            return dictionary[n]
