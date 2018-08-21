def merge_sort(n):
    if len(n) < 2:
        return n
    m = len(n) / 2
    left = n[:m]
    right = n[m:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
    result += left[i:]
    result += right[j:]
    return result


def quick_sort(ary):
    if len(ary) <= 1:
        return ary
    pivot = ary[0]
    min = [i for i in ary[1:] if i < pivot]
    max = [i for i in ary[1:] if i > pivot]
    return quick_sort(min) + [pivot] + quick_sort(max)


def quicksort(ary):
    def _quicksort(ary, low, high):
        if low < high:
            pivot = partition(ary, low, high)
            _quicksort(ary, low, pivot)
            _quicksort(ary, pivot + 1, high)

    def partition(ary, low, high):
        pivot = ary[low]
        while True:
            while ary[low] < pivot:
                low += 1
            while ary[high] > pivot:
                high -= 1
            if low >= high:
                return high
            ary[low], ary[high] = ary[high], ary[low]
            low += 1
            high -= 1

    _quicksort(ary, 0, len(ary) - 1)
    return ary


def bubble_sort(ary):
     length = len(ary) - 1
     sorted = False
     while not sorted:
         sorted = True
         for i in range(0,length):
             if ary[i] > ary[i+1]:
                  sorted = False
                  ary[i],ary[i+1]  = ary[i+1], ary[i]

     return ary
print(bubble_sort([3,2,1]))