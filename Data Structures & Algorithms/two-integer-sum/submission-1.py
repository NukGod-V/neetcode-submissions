class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        le = len(nums)
        for i in range(le):
            for j in range(i+1,le):
                if nums[i] + nums[j] == target:
                    return [i,j]