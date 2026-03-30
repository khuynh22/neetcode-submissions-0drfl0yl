class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0, 0, 0]
        for n in nums:
            colors[n] += 1
        print(colors)
        index = 0
        for i in range(len(colors)):
            for j in range (0, colors[i]):
                nums[index] = i
                index += 1
            
        return nums
