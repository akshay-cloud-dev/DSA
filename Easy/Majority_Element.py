from typing import List
class Solution():
    def majorityElement(self, nums:List[int]) ->int:
        count = {}
        res , maxCount = 0,0

        for n in nums:
            count[n] = 1 + count.get(n,0)
            res = n if count[n] > maxCount else res
            maxCount = max(count[n], maxCount)
        return res
nums = [2,2,3,3,4,4,5,5,5]
s = Solution()
print(s.majorityElement(nums))