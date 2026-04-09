class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ### Bucket sort
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        res = [[] for i in range(len(nums)+1)]
        for num, cnt in count.items():
            res[cnt].append(num)
        fnl = []
        for i in range(len(nums)+1):
            j = len(nums) - i 
            if len(res[j])> 0:
                for p in res[j]:
                    fnl.append(p)
            if len(fnl)==k:
                return fnl


   


        