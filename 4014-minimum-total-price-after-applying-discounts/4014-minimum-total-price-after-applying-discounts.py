class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        prices.sort(reverse= True)
        discounts.sort(reverse= True)
        total = 0
        for i in range(len(prices)):
            if i < len(discounts):
                total += prices[i] * (100 - discounts[i]) / 100
            else :
                total += prices[i]

        return total
