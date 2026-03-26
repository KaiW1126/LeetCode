class Solution:
    def isHappy(self, n: int) -> bool:
        self.seen = set()
        while n != 1:
            if n in self.seen:
                return False
            self.seen.add(n)
            n = self.get_sum(n)
        return True
    
    def get_sum(self,n):
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum