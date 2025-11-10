#two sum using the complement --> O(n)

def comp(nums, tar):
    dict = {}
    for i, val in enumerate(nums):
        complement = target - val
        if complement in dict:
            return [dict[complement], i]
        dict[val] = i
    return 'not possible'
        

nums = [ 2, 7, 11, 15]
target = 9
x = comp(nums, target)
print(x)