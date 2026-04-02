class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = defaultdict(int)
        final_list = []
        for i in nums:
            index[i]+=1
        arr = []
        for num, cnt in index.items():
            arr.append([cnt,num])
        arr.sort(reverse = True)
        for i in range(k):
            final_list.append(arr[i][1])
        return final_list