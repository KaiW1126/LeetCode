class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0  # 現在到達可能な最遠のインデックス
        
        for i in range(len(nums)):
            # 現在位置が到達可能範囲外なら失敗
            if i > max_reach:
                return False
            
            # 現在位置から到達可能な最遠距離を更新
            max_reach = max(max_reach, i + nums[i])
            
            # 最後まで到達可能なら成功
            if max_reach >= len(nums) - 1:
                return True
        
        return True