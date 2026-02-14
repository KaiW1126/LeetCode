class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        row,column = len(matrix),len(matrix[0])
        left,right,top,bottom = 0,column-1,0,row-1
        while left <= right and top <= bottom:
            for i in range(left,right+1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top,bottom+1):
                ans.append(matrix[i][right])
            right -= 1
            if top <= bottom:  # 1行だけ残った場合の重複を防ぐ
                for i in range(right,left-1,-1):
                    ans.append(matrix[bottom][i])
            bottom -= 1
            if left <= right:  # 1列だけ残った場合の重複を防ぐ
                for i in range(bottom,top-1,-1):
                    ans.append(matrix[i][left])
            left += 1
        return ans