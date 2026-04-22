class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1 
        count_zero = 0 
        total_zero = 1

        output = []
        for i in nums:
            if i ==0:
                count_zero+=1
                total = 0
            if count_zero >1:
                total_zero = 0
            if i!=0:
                total = total*i
                total_zero = total_zero*i
        
        for i in nums:
            if i==0:
                output.append(int(total_zero))
            else: 
                output.append(int(total/i))

        return output



                
                

        