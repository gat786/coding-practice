class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for a in target:
            if a in arr:
                arr.remove(a)
            else:
                return False
        return True