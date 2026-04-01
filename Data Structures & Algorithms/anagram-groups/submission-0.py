class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = {}
        final_list = []

        for i in range(len(strs)):
            arr = [0]*26
            for j in strs[i]:
                arr[ord(j)-ord('a')]+=1
            tup = tuple(arr)
            if tup in anagram_dict:
                anagram_dict[tup].append(strs[i])
            else:
                anagram_dict[tup] = [strs[i]]

        for key in anagram_dict:
            final_list.append(anagram_dict[key])

        return final_list