class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums2=nums
       
        nums+=nums2
        return nums