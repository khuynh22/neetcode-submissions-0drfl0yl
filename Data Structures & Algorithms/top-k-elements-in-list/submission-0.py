class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        
        sorted_occurrences = sorted(list(count_map.values()), reverse=True)[:k]

        res = []
        for num in count_map:
            if count_map[num] in sorted_occurrences:
                res.append(num)

        return res
        