class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            if max_area < (r - l) * min(height[r], height[l]):
                max_area = (r - l) * min(height[r], height[l])
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            elif height[l] == height[r] and height[l+1] > height[r-1]:
                l += 1
            else:
                r -= 1
        return max_area