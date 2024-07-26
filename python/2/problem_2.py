class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = []
        sums = 0
        for i in range(0, len(nums)):
            sums += nums[i]
            output.append(sums)
        return output