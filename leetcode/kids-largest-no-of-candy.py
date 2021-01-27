class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum = max(candies)
        return [True if a + extraCandies >= maximum else False for a in candies]
        