from typing import List
class Solution():
    def single(self, nums:List[int])->int:
        res = 0
        for n in nums:
            res = n ^ res
        return res
nums = [1,1,2,3,2,5,5]
S= Solution()
print(S.single(nums))