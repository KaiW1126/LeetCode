class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        # 二つの入力値から、回文の条件を満たす限り、左右に拡大していく関数
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # whileを抜けた時は s[l] != s[r] なので、一つ内側の範囲を返す
            return s[l+1:r]
        
        for i in range(len(s)):
            # 奇数の長さの時は真ん中は一文字を取る必要があるためiとiを渡す
            p1 = expand(i,i)
            # 偶数の長さの時は真ん中は二文字を取る必要があるためiとi+1を渡す
            p2 = expand(i,i+1)
            # 通常pythonはmaxで文字列を辞書順で比較してしまう。そのためkey=lenで長さを比較するように指定する
            res = max(res,p1,p2,key=len)
        
        return res