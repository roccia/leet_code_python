# lintcode
# [
#    [-5,-3,-1,0,1],
#    [-2,-1,0,0,1],
#    [0,11,12,12,14]
# ],
# return 5
# 给一个横向排序的且纵向也排序的的 n * m的矩阵， 问里面有几个负数


def find(nums):
    count = 0
    rows = len(nums)
    cols = len(nums[0])
    row = 0
    col = cols - 1
    while col >= 0 and row < rows:
        if nums[row][col] < 0:
            count += col + 1
            row += 1
        else:
            col -= 1
    return count


print(find([
    [-5, -3, -1, 0, 1],
    [-2, -1, 0, 0, 1],
    [0, 11, 12, 12, 14]
]))
