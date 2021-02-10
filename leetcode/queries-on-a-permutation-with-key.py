from collections import deque

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        start_list = deque([i for i in range(1,m+1)])
        
        answers_list =[]
        for i in queries:
            item_index = start_list.index(i)
            item = start_list[item_index]
            start_list.remove(item)
            start_list.appendleft(item)
            answers_list.append(item_index)
        
        return answers_list