class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        if len(strs) == 0: # if empty, return ""
            return ""
        elif len(strs) == 1: # if one string contained, return that string
            return shortest

        for i, val in enumerate(strs): # find the shortest length of string in strs
            if len(shortest) > len(val):
                shortest = val
        
        for i, val in enumerate(shortest): # find if char of same index match, 
            for j in strs:
                if (shortest[i] != j[i]):
                    return shortest[:i]  # otherwise, return the string without the character of current iteration
        return shortest
        