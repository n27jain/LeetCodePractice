#https://leetcode.com/problems/coin-change/

import sys

class Solution:
    def coinChange(self, coins, amount):
        dictionary = {}
        return self.coinChangeRecurse(coins,amount,0, dictionary)
    
    def coinChangeRecurse(self, coins, amount, numCoins, dictionary):
        if amount in dictionary: return dictionary[amount]
        if amount == 0: return numCoins
        if amount < 0: return False

        minCoins = sys.maxint
        found = False
        
        for index in range(len(coins)):
            coin = coins[index]
            i = index
            remainder = amount - coin
            numberFound = self.coinChangeRecurse(coins, remainder, numCoins+1);
            if(numberFound and numberFound < minCoins ):
                minCoins = numberFound
                # found = True
            # elif(found and numberFound > minCoins ):
            #     return minCoins
        
        if minCoins < sys.maxint:
            dictionary[amount] = minCoins
            return minCoins
        else: 
            dictionary[amount]  = -1
            return -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    

