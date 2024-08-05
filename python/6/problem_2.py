class Solution:
    def hammingWeight(self, n: int) -> int:
        bstring = "{0:b}".format(int(n))
        count = 0
        for i in range(0, len(bstring)):
            if bstring[i] == '1':
                count += 1
        return count