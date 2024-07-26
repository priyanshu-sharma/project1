class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = {}
        for i in nums:
            if i in output.keys():
                output[i] += 1
            else:
                output[i] = 1
        print(output)
        result = []
        for key, value in output.items():
            if value == 2:
                result.append(key)
        return result