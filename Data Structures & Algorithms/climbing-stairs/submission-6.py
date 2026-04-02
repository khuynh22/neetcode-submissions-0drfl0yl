class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        one_step = 2
        two_step = 1

        for i in range(3, n + 1):
            temp = two_step + one_step
            two_step = one_step
            one_step = temp
        
        return one_step