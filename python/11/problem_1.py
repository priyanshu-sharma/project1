class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = s.lower()
        ft = ''
        for i in range(0, len(k)):
            if (ord(k[i]) >= 97 and ord(k[i]) <= 122) or (ord(k[i]) >= 48 and ord(k[i]) <= 57):
                ft += k[i]
        left, right = 0, len(ft) - 1
        while left <= right:
            if ft[left] == ft[right]:
                left += 1
                right -= 1
            else:
                return False
        return True