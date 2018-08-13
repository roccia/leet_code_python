# Given two arrays, write a function to compute their intersection.
#
# Example:
# Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].
#
# Note:
# Each element in the result should appear as many times as it shows in both arrays.
# The result can be in any order.


def intersect(nums1, nums2):
    h = {}
    res = []
    for n in nums1:
        if n not in h:
            h[n] = 1
        else:
            h[n] += 1
    for i in nums2:
        if i in h and h[i] > 0:
            res.append(i)
            h[i] -= 1
    return res 


print(intersect([1, 2, 2, 1], [2, 2]))
