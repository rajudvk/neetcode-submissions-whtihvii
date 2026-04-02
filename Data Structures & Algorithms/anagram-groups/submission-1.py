class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Cleaned version of code using defaultdict and .values
        anagram_dict = defaultdict(list)
        for s in strs:
            cnt = [0]*26
            for i in s:
                cnt[ord(i)-ord('a')]+=1
            anagram_dict[tuple(cnt)].append(s)
        return list(anagram_dict.values())