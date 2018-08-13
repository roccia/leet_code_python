# Given an array of integers and an integer k,
# you need to find the total number of continuous subarrays whose sum equals to k.


def check_pair(ary, target):
    if len(ary) <= 1:
        return 0
    hash = {}
    res = []
    for i in range(0, len(ary) - 1):
        temp = target - ary[i]
        if temp in hash:
            res.append([temp, ary[i]])
        hash[ary[i]] = 1
    return res


print(check_pair([1, 2, 3, 4, 5, 6], 6))
