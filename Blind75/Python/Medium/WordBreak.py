class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s)+1) #何もないから文字も含めるために+1
        #dp[i]はsの0からi番目までの文字列が単語に分割できるかを表す
        #dp[0]は空文字列なのでTrue
        dp[0] = True
        for i in range(1,len(s)+1):
            #各 i に対して、j を 0 から i-1 まで試す
            #条件：dp[j] が True かつ s[j:i] が辞書に存在するか確認
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[len(s)]