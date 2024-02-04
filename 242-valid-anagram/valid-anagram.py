class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ##Time o(nlogn) space o(1)
       ## if sorted(s)==sorted(t):
        ##    return True

        ##return False

        if len(s)!=len(t):
            return False
        cT,cS={},{}

        for i in range(len(s)):
            cS[s[i]]=1+cS.get(s[i],0)
            cT[t[i]]=1+cT.get(t[i],0)

        for c in cT:
            if cT[c]!=cS.get(c,0):
                return False

        return True
            
        