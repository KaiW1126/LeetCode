class Solution:
    def numDecodings(self, s: str) -> int:
        # 0が(len(s)+1)個入ったリストを作るという初期化
        dp = [0] * (len(s) + 1) 
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if s[i - 2] == "1" or (s[i - 2] == "2" and s[i - 1] <= "6"):
                dp[i] += dp[i - 2]
        return dp[len(s)]
    