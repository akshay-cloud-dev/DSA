def merge_sort(l1:list, l2:list) ->list:
    p1, p2 = 0, 0
    merge_list = []
    while p1<len(l1) and p2<len(l2):
        if l1[p1]<=l2[p2]:
            merge_list.append(l1[p1])
            p1+=1
        else:
            merge_list.append(l2[p2])
            p2+=1
    merge_list.extend(l1[p1:])
    merge_list.extend(l2[p2:])
    return merge_list

def combine_list(l1_unsorted:list, l2_unsorted:list)->list:
    l1_sorted = sorted(l1_unsorted)
    l2_sorted = sorted(l2_unsorted)
    print(l1_sorted, l2_sorted)

    return merge_sort(l1_sorted, l2_sorted)

l1 = [555,6,7,8,11,23]
l2 = [5, 2, 77, 9, 1, 4]

result = combine_list(l1,l2)
print(result)
    