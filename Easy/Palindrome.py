

class Solution:
    def isPalindrome(self, x: int) -> bool:
        #ex) x = 57875
        
        copy = x    #copy value of x
        track = 0   
        while (x>0):
            track = (track*10) + (x%10) # track becomes, 5->57->578->5787->57875  #나머지 값 + 그전값*10
            x = x//10                   # x becomes, 57875->5787->578->57->5->0   #나눈 값
        return copy == track

