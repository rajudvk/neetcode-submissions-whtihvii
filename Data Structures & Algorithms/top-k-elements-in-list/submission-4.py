class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Not using lambda and sorted helped with space and time complexity 
        index = {}
        final_list = []
        for i in nums:
            index[i] = 1 + index.get(i,0)
        arr = []
        for num, cnt in index.items():
            arr.append([cnt,num])
        arr.sort(reverse = True)
        for i in range(k):
            final_list.append(arr[i][1])
        return final_list