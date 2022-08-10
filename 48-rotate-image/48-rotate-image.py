class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        
        # Transpose
            
        
        for i in range(size):
            for j in range(i+1,size):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            matrix[i].reverse()