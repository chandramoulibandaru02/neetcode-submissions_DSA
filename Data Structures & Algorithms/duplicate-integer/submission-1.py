class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=len(nums)
        b=set(nums)

        if a==len(b):
            return False
        return True    