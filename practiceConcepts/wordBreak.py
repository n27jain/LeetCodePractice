class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sC = [""] # initial word is currently empty
        for i, char in enumerate(s):
            isFound = False
            for j, word in enumerate(sC):
                sC[j] = word + char
                if sC[j] in wordDict:
                    isFound = True
                    if i == len(s) - 1: # if this is the last char and the word has been found -> success!
                        return True
                    # iteratively search for current word in case it is actually longer. 
                
            if isFound == True:
                #Add an empty string that will accept only the new characters to find a potential other word
                sC.append("")
                   
        return False # we were not successful in finding the sol 
