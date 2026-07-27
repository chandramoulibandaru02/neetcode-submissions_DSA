class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        strs.sort()
        left =strs[0]
        right=strs[-1]
        for i in range(min(len(left),len(right))):
            if left[i]!=right[i]:
                return res
            res+=left[i]
        return res        
