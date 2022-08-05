class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
        num = ""
        values = []
        for i in range(n):
            values.append(i+1)
            
        for i in range(0 , n):
            remains = n-i-1
            combo = self.factorial(remains)
            dec = 0
           
            while k > combo:
                dec += 1
                k -= combo
            
            num += str(values[dec])
            del values[dec]
            
        
        return num
            
                
        
    def factorial(self, num):
        output = 1
        while num > 1:
            output *= num
            num -= 1
        return output
            
        