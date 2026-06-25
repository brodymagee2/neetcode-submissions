class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashy = {}

        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in hashy:
                return [hashy[wanted], i]
            hashy[nums[i]] = i