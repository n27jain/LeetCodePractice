# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

#Brute force
class Solution(object):
    def maxProfit(self, prices):
        maximum = 0
        for i in range(len(prices)):
            j = i+1
            while j < len(prices):
                diff = prices[j]-prices[i]
                maximum = max(diff, maximum)
        return maximum


# finding smallest number before current index difference 
class Solution(object):
    def maxProfit(self, prices):
        maximum = 0
        smallest = prices[0]
        for num in prices:
            if(num < smallest):
                smallest = num
            elif(num - smallest > maximum):
                maximum = num - smallest
        return maximum