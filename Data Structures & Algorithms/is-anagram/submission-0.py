class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}
        for v in s:
            if v in dic1:
                dic1[v]+=1
            else:
                dic1[v] = 1
        for h in t:
            if h in dic2:
                dic2[h]+=1
            else:
                dic2[h] = 1
        if dic1 == dic2:
            return True
        else:
            return False