class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count_map = {}
        for num in nums:
            if num in count_map.keys():
                return True
            else:
                count_map[num] = 1
        return False