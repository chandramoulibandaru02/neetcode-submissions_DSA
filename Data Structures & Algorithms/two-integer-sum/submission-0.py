class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=len(nums)
        li=[]
        for i in range(0,a):
            for j in range(i+1,a):
                if nums[i]+nums[j]==target:
                    li.append(i)
                    li.append(j)
                    return li                   