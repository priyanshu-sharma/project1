class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        pre = 1
        for i in range(0, len(nums)):
            output.append(pre)
            pre *= nums[i]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output