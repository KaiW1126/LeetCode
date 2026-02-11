from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            # 水の量は (底辺の長さ) * (左右の高さの低い方) で決まる
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            
            # 高さが低い方のポインタを動かすことで、より高いラインを探す
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


                    