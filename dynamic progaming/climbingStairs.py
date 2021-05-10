
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
