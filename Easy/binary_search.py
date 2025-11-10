class Solution():
    def search_bin(self, lis, key):
        low = 0 
        high = len(lis)-1
        if not lis:
            return "failed"
        while low <= high:
            mid = (high + low) //2
            if lis[mid] == key:
                print(f"The searched element is in the pos {mid}")
                return mid
            elif lis[mid] >key:
                high = mid -1
            else:
                low = mid+1
        print("key not found")
        return -1

listu = [3,5,6,7,8,9,10]
key = 10
s = Solution()
ans = s.search_bin(listu, key)
print(ans)