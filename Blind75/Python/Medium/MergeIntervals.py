class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        
        for interval in intervals:
            # mergedが空、または現在の区間が前の区間と重ならない場合
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # 重なる場合、終了位置を更新
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged