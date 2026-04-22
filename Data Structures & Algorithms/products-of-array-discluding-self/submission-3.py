class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ### Without division
        prefix = 1
        suffix = nums[-1]
        res = [1]
        for i in range(len(nums)-1):
            prefix *=nums[i]
            res.append(prefix)
        for i in range(len(nums)-2,-1,-1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
            



            







        return output



                
                

        