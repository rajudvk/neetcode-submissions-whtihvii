class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = {}
        arr = []
        for i in nums:
            index[i] = index.get(i,0)+1
        for num, cnt in index.items():
            arr.append((cnt,num))
        
        heapq.heapify(arr)

        return [i[1] for i in heapq.nlargest(k, arr)]


        