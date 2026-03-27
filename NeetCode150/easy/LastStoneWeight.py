class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            y = stones.pop()
            x = stones.pop()
            if y > x:
                stones.append(y-x)
            stones.sort()
        return stones[0] if stones else 0