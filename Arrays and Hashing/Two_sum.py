#Two sum problem using hashing

from typing import List


class Solution():
    def twosum(self, nums:List[int], target:int)->List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
sol = Solution()
target = 5
nums = [2,2,3,4,5,6]
print(sol.twosum(nums, target))