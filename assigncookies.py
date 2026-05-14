class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l = 0
        r = 0 
        s.sort()
        g.sort()
        count = 0

        while l < len(g) and r < len(s):
            if s[r] >= g[l]:
                count+=1
                l+=1
            r+=1
        return count
