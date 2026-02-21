#問題の制約は1<=n<=500, 1<=nums[i]<=1000
#よって1000は10ビットあれば表現できる
#Pythonにおけるビット演算は基本無制限
#x << n : xをnビット左にシフトする（x * 2**n）
#x >> n : xをnビット右にシフトする（x // 2**n）
#x & n : xとnのビットごとのAND演算
#x | n : xとnのビットごとのOR演算
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10 #上位10ビットは空っぽ
            nums[i] = nums[i] | nums[i + n] #下位10ビットに元のnums[i+n]を代入
        
        j=2*n-1
        # 開始時はn-1,終了は0まで含めるため-1,底から逆順
        for i in range(n-1,-1,-1):
            y = nums[i] & (2**10 - 1)
            #2**10-1が下位１０ビット全てが一であるからそれのandで下位10ビットだけ抽出
            #上位は全て０だから、nums[i]の上位10ビットはすべて0
            x = nums[i] >> 10
            nums[j] = y
            nums[j-1] = x
            j -= 2
        return nums