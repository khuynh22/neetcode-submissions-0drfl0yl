class Solution:
    def rob(self, nums: List[int]) -> int:
        house1, house2 = 0, 0

        for i in range(len(nums)):
            temp = max(house1 + nums[i], house2)
            house1 = house2
            house2 = temp

        return house2
