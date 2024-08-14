class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for i in s:
            if i not in s_dict.keys():
                s_dict[i] = 0
            else:
                s_dict[i] += 1
        
        for i in t:
            if i not in t_dict.keys():
                t_dict[i] = 0
            else:
                t_dict[i] += 1
        s_output = []
        for key, value in s_dict.items():
            s_output.append("{}_{}".format(key, value))
        t_output = []
        for key, value in t_dict.items():
            t_output.append("{}_{}".format(key, value))
        if set(s_output) != set(t_output):
            return False
        return True