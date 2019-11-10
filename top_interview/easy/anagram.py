from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = defaultdict(int)
        for c in s:
            s_dic[c] += 1
        
        for c in t:
            if c not in s_dic:
                return False
            s_dic[c] -= 1
            if s_dic[c] == 0:
                del s_dic[c]
        
        return True if len(s_dic) == 0 else False        
