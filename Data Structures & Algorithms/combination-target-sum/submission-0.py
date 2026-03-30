class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr_list, total):
            if total == target:
                res.append(curr_list.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            curr_list.append(nums[i])
            dfs(i, curr_list, total + nums[i])
            curr_list.pop()
            dfs(i + 1, curr_list, total)
        
        dfs(0, [], 0)
        return res