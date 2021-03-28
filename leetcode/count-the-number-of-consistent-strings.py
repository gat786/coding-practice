class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set([x for x in allowed])
        wordsSetList = [set([x for x in word]) for word in words]
        count = 0
        for i in wordsSetList:
            if i - allowedSet == set():
                count += 1
        return count