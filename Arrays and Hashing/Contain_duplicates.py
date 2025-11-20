#contain duplicate value

from typing import List
class Solution():
    def containduplicate(self, nums:List[int])->int:
        hashset = set()
        for n in nums:
            if n in hashset:
                return n
            hashset.add(n)
        return False
s = Solution()
nums = [1,2,3,2,4]
print(s.containduplicate(nums))
                

        