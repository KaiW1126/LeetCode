class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total = m + n - 2
        # (m+n-2)! を計算
        x = 1
        for i in range(total, m-1, -1):
            x *= i
        # (n-1)! を計算
        y = 1
        for i in range(1, n):
            y *= i
        # C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
        return x // y