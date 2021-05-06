import re

class Solution(object):
    
    def strongPasswordChecker(self, password):
        count = 0
        length = len(password)
        lower, upper, digit= self.baseCase(password)
        
        prevChar = None
        numberConsecutive = 0
        
        for i in range(len(password)):
            char = password[i]
            if(prevChar == char):
                numberConsecutive += 1
                
                if(numberConsecutive == 3):
                    count += 1
                    # we have 3 in a row
                    if(i < len(password)-1 and password[i+1] == prevChar):
                        # there is a 4 sequence so we need to replace we cannot simply remove and must replace
                        if(not lower):
                            lower = True
                        elif(not upper):
                            upper = True
                        elif(not digit):
                            digit = True
                    else:
                        # we only have 3 in a row. Replacement is an option
                        if(length < 6): # we should add
                            if(not lower):
                                lower = True
                            elif(not upper):
                                upper = True
                            elif(not digit):
                                digit = True
                        elif(length > 20): # we should remove since we are going to have to do this anyways
                            length -= 1
                    numberConsecutive = 0
                            
            else:
                prevChar = char
                numberConsecutive = 0
        
        if(not lower):
            count += 1
            lower = True
            if(length < 6): # we must add a lowercase char
                length += 1
            
        if(not upper):
            count += 1
            upper = True
            if(length < 6): # we must add a uppercase char
                length += 1
        
        if(not digit):
            count += 1
            digit = True
            if(length < 6): # we must add a digit char
                length += 1
        if(length<6):
            count = count + (6-length)
        elif(length>20):
            count = count + (length - 20)
            
        return count
                
                
            
    def baseCase(password):
        lower = False
        upper = False
        digit = False
        
        for char in password:
            if(char.islower()):
                lower = True
            elif(char.isupper()):
                upper = True
            elif(char.isdigit()):
                digit = True
           
        return lower, upper, digit

