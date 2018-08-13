# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
#     The same repeated number may be chosen from C unlimited number of times.
#
#         Note:
#     All numbers (including target) will be positive integers.
#     The solution set must not contain duplicate combinations.
#     For example, given candidate set [2, 3, 6, 7] and target 7,
#      A solution set is:
#              [ [7],[2, 2, 3] ]


def combination_sum_I(candi, target):
    res = []
    temp = []
    new_candi = sorted(candi)
    backtrack(new_candi, target, 0, temp, res)
    return res


def backtrack(candi, target, index, temp, res):
    if target < 0:
        return
    elif target == 0:
        res.append(temp)
    else:
        for i in range(index, len(candi)):
            if candi[i] > target:
                break
            backtrack(candi, target - candi[i], i, temp + [candi[i]], res)


# Given a collection of candidate numbers (candidates) and a target number (target),
# find all unique combinations in candidates where the candidate numbers sums to target.
#
#     Each number in candidates may only be used once in the combination.
#
#     Note:
#
#     All numbers (including target) will be positive integers.
#     The solution set must not contain duplicate combinations.
#     Example 1:
#
#     Input: candidates = [10,1,2,7,6,1,5], target = 8,
#     A solution set is:
#                        [
#                            [1, 7],
#                            [1, 2, 5],
#                            [2, 6],
#                            [1, 1, 6]
#                        ]
# Example 2:
#
#     Input: candidates = [2,5,2,1,2], target = 5,
#     A solution set is:
#                        [
#                            [1,2,2],
#                            [5]
#                        ]

def combination_sum_II(candi, target):
    res = []
    temp = []
    new_candi = sorted(candi)
    backtrack2(new_candi, target, 0, temp, res)
    return res


def backtrack2(candi, target, index, temp, res):
    if target < 0:
        return
    if target == 0:
        res.append(temp)

    for i in range(index, len(candi)):
        # To avoid overcounting, we just ignore the duplicates
        # after the first element.
        if i > index and candi[i] == candi[i - 1]:
            continue
        # If the current element is bigger than the assigned target, there is
        # no need to keep searching, since all the numbers are positive
        if candi[i] > target:
            break
        # We change the start to `i + 1` because one element only could
        # be used once
        backtrack2(candi, target - candi[i], i + 1, temp + [candi[i]], res)


print(combination_sum_I([2, 3, 6, 7], 7))
print(combination_sum_II([10, 1, 2, 7, 6, 1, 5], 8))
