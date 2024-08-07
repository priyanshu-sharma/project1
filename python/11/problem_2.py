class Solution:
    def isValid(self, s: str) -> bool:
        output = []
        for i in range(0, len(s)):
            if s[i] in ['(', '[', '{']:
                output.append(s[i])
            elif (s[i] == ')' and len(output) > 0 and output[len(output) - 1] == '(') or (s[i] == ']' and len(output) > 0 and output[len(output) - 1] == '[') or (s[i] == '}' and len(output) > 0 and output[len(output) - 1] == '{'):
                output.pop()
            else:
                return False
        if len(output) == 0:
            return True
        return False