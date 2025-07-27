class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    return [nums[i],nums[j]]

nums = list(map(int, input().split()))
target = int(input())
s = Solution()
print(s.twoSum(nums,target))