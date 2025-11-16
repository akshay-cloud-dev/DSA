#Missing Number
from typing import List
class Solution():
    def num(self, inp:List[int])->int:
        if not inp:
            raise ValueError("Input list cannot be empty")
        n = len(inp)
        expected_sum = n*(n+1)//2
        actual_sum = sum(inp)
        return expected_sum-actual_sum
if __name__ == '__main__':
    s = Solution()
    inp=[3,0,1,2,5]
    ans = s.num(inp)
    print(ans)
#Output: 2