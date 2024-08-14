class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        output = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    output.append([i, j])
        for val in output:
            a, b = val
            for i in range(0, len(matrix[0])):
                matrix[a][i] = 0
            for i in range(0, len(matrix)):
                matrix[i][b] = 0 
        