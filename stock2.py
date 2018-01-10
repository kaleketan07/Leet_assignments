def maxProfit(prices):

    if len(prices) == 1:
        return prices[0]
    elif len(prices) == 0:
        return 0
    else:
        maxp = 0
        min = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                maxp += prices[i] - min
                min = prices[i]

        return maxp

if __name__ == '__main__':
    print maxProfit([4, 7, 3, 11, 8, 6, 2, 13])

