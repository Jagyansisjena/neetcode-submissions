import numpy as np
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        arr = np.array(matrix)

        return target in arr
        