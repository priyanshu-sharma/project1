class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = []
        output.extend(nums)
        output.extend(nums)
        return output