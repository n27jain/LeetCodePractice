#question
# A password is considered strong if the below conditions are all met:

# It has at least 6 characters and at most 20 characters.
# It contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
# It does not contain three repeating characters in a row (i.e., "...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# Given a string password, return the minimum number of steps required to make password strong. if password is already strong, return 0.

# In one step, you can:

# Insert one character to password,
# Delete one character from password, or
# Replace one character of password with another character.




class Solution(object):
    
    def strongPasswordChecker(self, password):
        count = 0
        length = len(password)
        lower, upper, digit= self.baseCase(password)
        # print(lower, upper, digit)
        prevChar = None
        numberConsecutive = 0
        
        for i in range(len(password)):
            #print(numberConsecutive)
            char = password[i]
            if(prevChar == char):
                numberConsecutive += 1
                
                if(numberConsecutive == 2):
                    # print(count)
                    #we try and replace first

                    if(length < 6): # we should try and add first
                        length += 1
                        count += 1
                        if(not lower):
                            lower = True
                        elif(not upper):
                            upper = True
                        elif(not digit):
                            digit = True
                    if(not lower):  # we should try to replace second
                        lower = True
                        count += 1
                    elif(not upper):
                        upper = True
                        count += 1
                    elif(not digit):
                        digit = True
                        count += 1
                    elif(length > 20): # must remove since all other cases have been met
                        if(i < len(password)- 1 and password[i+1] == prevChar): # not the last char on list and next char matches
                           i += 1
                           count += 1
                           length -=1
                           while(i <= len(password) - 1 and password[i] == prevChar):
                               count +=1
                               i+=1
                               length -=1
                        else:
                            length -=1
                            count += 1
                    numberConsecutive = 0
                    prevChar = None
            else:
                prevChar = char
                numberConsecutive = 0
        
        print(lower, upper, digit, count, length)


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
                
                
       
    def baseCase(self, password):
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


