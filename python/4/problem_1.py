class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        output = {}
        for i in range(0, len(nums)):
            if nums[i] in output.keys():
                return True
            else:
                output[nums[i]] = 1
        return False