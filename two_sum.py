class TwoSum:
    def two_sum(self,nums,target):
        hash = {}

        for i in range(len(nums)):
            if nums[i] in hash:
               return [hash[nums[i]],i]
            else:
               hash[target - nums[i]] = i 
        return -1,-1

class ThreeSum:
    def three_sum(self,nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1 , len(nums) -1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append((nums[i],nums[l],nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
        return res
