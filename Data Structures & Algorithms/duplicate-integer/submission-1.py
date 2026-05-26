class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for v in nums:
            count = 0
            for x in nums:
                if v == x:
                    count+=1
            if count >= 2:
                return True
        return False

        