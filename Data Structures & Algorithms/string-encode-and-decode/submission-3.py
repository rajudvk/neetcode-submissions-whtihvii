class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            str_len = len(i)
            res += str(str_len)+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        i = j = 0
        res = []
        while i <len(s):
            if s[i] =="#":
                str_len = int(s[j:i])
                j = i+str_len+1
                res.append(s[i+1:j])
                i = j
            else:
                i+=1
        return res


                    




