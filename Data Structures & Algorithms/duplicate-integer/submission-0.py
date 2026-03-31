class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_set = len(set(nums))
        len_list = len(list(nums))

        if len_set != len_list:
            return True 
        else:
            return False

        