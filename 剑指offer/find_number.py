# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维 数组和一个整数，判断数组中是否含有该整数。


def find(matrix, target):
    if not matrix or len(matrix) < 1 or len(matrix[0]) < 1:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    row = 0
    col = cols - 1

    while 0 <= row <= rows and 0 <= col <= cols:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False
