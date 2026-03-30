class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}
        for i in range(len(nums)):
            two_sum[nums[i]] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in two_sum and i != two_sum[diff]:
                return [i, two_sum[diff]]