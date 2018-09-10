class KthLargest:
    def k_largest(self,nums,k):
        self.build_max_heap(nums)
        nums_size = len(nums)
        index = 0
        while index < k:
            ele_max = self.extract_max(nums,nums_size)
            nums_size -= 1
            index += 1
        return ele_max


    def build_max_heap(self,nums):
        for i in range((len(nums)//2 - 1),0):
            self.max_heapfiy(nums,len(nums),i)
        return nums

    def extract_max(self,nums,size):
        root = nums[0]
        nums[0] = nums[size - 1]
        self.max_heapfiy(nums,size-1,0)
        return root

    def max_heapfiy(self,keys,size,index):
        left = 2*index + 1
        right = 2*index + 2
        if left < size and keys[left] > keys[index]:
            largest = left
        else:
            largest = index

        if right < size and keys[right] > keys[largest]:
            largest = right

        if largest != index:
            keys[index] , keys[largest] = keys[largest],keys[index]
            self.max_heapfiy(keys,size,largest)

k = KthLargest()
print(k.k_largest([9, 4, 5, 2, 1, 23, 55, 88, 74, 89],3))