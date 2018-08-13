# Given a n x n matrix where each of the rows and columns are sorted
#  in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order,
# not the kth distinct element.
#
#     Example:
#
#     matrix = [
#         [ 1,  5,  9],
#         [10, 11, 13],
#         [12, 13, 15]
#     ],
#         k = 8,
#
#         return 13.


def kth_smallest(matrix, k):
    return sorted(flatten(matrix))[k - 1]


def flatten(matrix):
    new_list = []
    for sublist in matrix:
        for i in sublist:
            new_list.append(i)
    print(new_list)
    return new_list


#查找一行需要log(n) ，有n行所以nlog(n)，
# 最坏下需要查找log(X)次（X= int最大值的时候logX仅仅才为32），X为最大最小数差值。
# 所以总复杂度为O(nlogn *  logX)
def kth_smallest_bs(matrix, k):
    m, n = len(matrix), len(matrix[0])
    low = matrix[0][0]
    high = matrix[m - 1][n - 1]

    while low < high:
        mid = low + (high - low) // 2
        print('!!!!')
        print(mid)
        count = 0
        j = len(matrix[0]) - 1
        print('#####')
        print(j)
        # count how many number of elements in the matrix less than middle value
        for i in range(0, len(matrix)):
            print(i,j)
            print(matrix[i][j])
            while j > 0 and matrix[i][j] > mid:
                print('$$$$$')
                print(j)
                j -= 1
            count += j + 1
            print('count:')
            print(count)
        if count < k:
            low = mid + 1
        else:
            high = mid
    return low


print(kth_smallest([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 8))

print(kth_smallest_bs([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 8))
