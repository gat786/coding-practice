class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        data_points = []
        for point in points:
            data_points.append(point[0])
            
        data_points.sort()
        
        largest_diff = 0
        
        for index,num in enumerate(data_points[:-1]):
            if (data_points[index+1] - data_points[index]) > largest_diff:
                largest_diff = data_points[index+1] - data_points[index]
        
        return largest_diff