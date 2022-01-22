class Solution:
    def isValid(self, s: str) -> bool:
        #if key in dictionary:  #whether key exists in dictionary
        
        #last in first out
        stack = []
        hash_table = {']':'[', # don't know why it gives keyerror when I put open brackets in keys
               ')': '(',
               '}': '{'}
        for i in s:
            if i in hash_table.values():
                stack.append(i)
            elif i in hash_table.keys():
                if stack == [] or stack.pop() != hash_table[i]:
                    # if i dont check stack is empty, gives error cuz I try to pop of empty list otherwise.
                    return False
            else:
                continue
        return len(stack) == 0

# class Solution:
#     def isValid(self, s: str) -> bool:
#         #if key in dictionary:  #whether key exists in dictionary
        
#         #last in first out
#         stack = []
#         hash_table = {'[':']',
#                '(': ')',
#                '{': '}'}
#         for i in s:
#             if i in hash_table:
#                 stack.append(i)
#             elif i in hash_table.values():
#                 if stack == [] or hash_table[i] != stack.pop():
#                     return False
#             else:
#                 continue
#         return True
                    
                
        
        