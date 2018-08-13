# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


def search_range(nums, target):
    if len(nums) == 0:
        return [-1, -1]
    left_idx = search(nums, target, True)
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]
    return [left_idx, search(nums, target, False) - 1]


def search(nums, target, left):
    left = 0
    right = len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > target or (left and nums[mid] == target):
            right = mid
        else:
            left = mid + 1

    return left


print(search_range([5, 7, 7, 8, 8, 10], 8))
