class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 配列をSetに変換する（検索がO(1)になる）
        num_set = set(nums)
        longest = 0
        
        for n in num_set:
            if (n - 1) not in num_set: #例えば3-1で２がnum_setにあるか探してあれば、3はスタート地点ではなくなる
                length = 1
                
                # 自分より1大きい数字が存在する限り、連続しているので数え続ける
                while (n + length) in num_set:
                    length += 1
                    
                # 途切れたら、過去の最大記録（longest）を更新する
                longest = max(longest, length)
                
        return longest