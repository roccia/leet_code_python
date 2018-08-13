# Given an array nums containing n + 1 integers where each integer
# is between 1 and n (inclusive),
# prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
#     Note:
#     You must not modify the array (assume the array is read only).
#     You must use only constant, O(1) extra space.
#     Your runtime complexity should be less than O(n2).
#         There is only one duplicate number in the array,
# but it could be repeated more than once.


# binary search
def find_duplicate(nums):
    low = 1
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        count = 0
        for n in nums:
            if n <= mid:
                count += 1
        if count <= mid:
            low = mid + 1
        else:
            high = mid
    return low


# two pointer
def find_dup(nums):
    slow = nums[0]
    fast = nums[slow]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


print(find_duplicate([3, 1, 3, 4, 2]))
print(find_dup([3, 1, 3, 4, 2]))
