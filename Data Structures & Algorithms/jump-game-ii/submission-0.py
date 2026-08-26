class Solution:
    def jump(self, nums: List[int]) -> int:
        count_jump = 0
        l, r = 0, 0

        while r < len(nums) - 1:
            largest_range = 0
            for i in range(l, r + 1):
                largest_range = max(largest_range, i + nums[i])
            l = r + 1
            r = largest_range
            count_jump += 1
        
        return count_jump