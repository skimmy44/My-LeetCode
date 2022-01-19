class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        dict = {}
        for i, val in enumerate(strs):
            dict[val] = i
        
        reVal = ""
        