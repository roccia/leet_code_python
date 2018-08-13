# Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.
#
# Note:
# You may assume that nums1 has enough space (size that is greater or equal
# to m + n) to hold additional elements from nums2.
# The number of elements initialized in nums1 and nums2
# are m and n respectively.


def merge_ary(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = m + n - 1  # index of the last element of the merged array
    # compare A an B from back, put larger element to A
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1
        else:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
    while j >= 0: # if B is longer than A, just copy the rest of B to A
        nums1[k] = nums2[j]
        k -= 1
        j -= 1
    return nums1
