from typing import List
class Solution():
    def single(self, lis:List)->int:
        count_dict = {}
        for i in lis:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        for key, value in count_dict.items():
            if value ==1:
                return key
        return None
lis = [3,5,6,5,4,4,3,9] 
s = Solution() 
print(s.single(lis))
    