class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices_map = {}
        for i, num in enumerate(nums):
            indices_map[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in indices_map and indices_map[diff] != i:
                return [i, indices_map[diff]]
            
        return []