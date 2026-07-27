class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        di={}
        
        for s in strs:
            sorted_word="".join(sorted(s))
            if sorted_word not in di:
                di[sorted_word]=[]
            di[sorted_word].append(s)

        return list(di.values())