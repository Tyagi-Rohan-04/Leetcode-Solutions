"""
LeetCode Romant to Integer question

"""


class Solution:
    def romanToInt(self, s: str) -> int:
        lookup = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        N = len(s)
        i = N-1
        count = 0
        while i >= 0:
            if i<N-1 and lookup[s[i]]<lookup[s[i+1]]:
                count -= lookup[s[i]]
            else:
                count += lookup[s[i]]
            i-=1
        return(count) 