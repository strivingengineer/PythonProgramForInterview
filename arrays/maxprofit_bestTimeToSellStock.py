
maintainer = 'strivingengineer'

'''

Leetcode 121. Best Time to Buy and Sell Stock

Link to problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day 
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 
Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

Solution:

To maximize the profit we have to minimize the buy cost and we have to sell it at maximum price. 

Declare a minprice variable to store the buy cost and maxprofit to store the maximum profit.
Initialize the minprice variable to the first element of the prices array.
Iterate over the prices array and check if the current price is minimum or not.
If the current price is minimum then buy on this ith day.
If the current price is greater than the previous buy then make profit from it and maximize the maxprofit.
Finally, return the maxprofit.

Time/ Space complexity: O(n) / O(1)

'''


def maxProfit(prices):
    if not prices:
        return 0

    maxprofit = 0

    minprice = prices[0]

    for price in range(1, len(prices)):
        if prices[price] < minprice:
            minprice = prices[price]
        if prices[price] - minprice > maxprofit:
            maxprofit = prices[price] - minprice

    return maxprofit

