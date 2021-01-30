class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for a in accounts:
            money = sum(a)
            if money > maximum:
                maximum = money
        return maximum