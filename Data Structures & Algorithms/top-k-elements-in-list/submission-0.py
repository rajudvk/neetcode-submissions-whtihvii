class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        index = defaultdict(int)
        final_list = []
        for i in nums:
            index[i]+=1
        sort_index = sorted(index.items(), key = lambda x:x[1], reverse = True)
        for i in range(k):
            final_list.append(sort_index[i][0])

        return final_list


        
        
        