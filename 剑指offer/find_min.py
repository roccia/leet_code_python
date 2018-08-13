# 要求：把递增数组的前面部分数字移到队尾，求数组中的最小值，例如[3,4,5,6,1,2]
#
# 思路：使用二分法，但要考虑[1, 0, 0, 1]这种数据，只能顺序查找


def find_min(nums):
    if not nums:
        return False
    first = 0
    last = len(nums) - 1
    while nums[first] >= nums[last]:
        if last - first == 1:
            return nums[last]
        mid = (first + last) // 2
        if nums[first] <= nums[mid]:
            first = mid
        if nums[last] >= nums[mid]:
            last = mid

    return nums[0]


print(find_min([1, 0, 0, 1]))
