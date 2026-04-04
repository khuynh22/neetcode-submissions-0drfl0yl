class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        
        one_back = 1
        two_back = 2

        for i in range(3, n + 1):
            temp = one_back + two_back
            one_back = two_back
            two_back = temp
        
        return two_back