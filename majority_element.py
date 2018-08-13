# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element
# always exist in the array.


def majority_element(nums):
    h = {}
    for n in nums:
        if not n in h:
            h[n] = 1
        else:
            h[n] += 1

    for key, value in h.items():
        if value > len(nums) // 2:
            return key


print(majority_element([6, 5, 5]))
