class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        s_freq = {}
        t_freq = {}

        for i, c in enumerate(s):
            if c in s_freq:
                s_freq[c] += 1
            else:
                s_freq[c] = 1
        
            if t[i] in t_freq:               
                t_freq[t[i]] += 1
            else: 
                t_freq[t[i]] = 1

        return s_freq == t_freq