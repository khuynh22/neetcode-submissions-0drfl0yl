# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def _swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
    
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        sol = [pairs.copy()] if pairs else []
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                self._swap(pairs, j, j + 1)
                j -= 1
            
            sol.append(pairs.copy())
        
        return sol
                