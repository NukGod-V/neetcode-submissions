class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "#" + s
        return st 

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            le = int(s[i:j])
            res.append(s[j+1:le+1+j])
            i = le + 1 + j
        return res

