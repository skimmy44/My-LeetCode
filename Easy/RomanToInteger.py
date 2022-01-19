class Solution:
    def romanToInt(self, s: str) -> int: #keys are always string
        romanHash = {'I':1,
                    'V':5,
                    'X':10,
                    'L':50,
                    'C':100,
                    'D':500,
                    'M':1000}
        reVal = 0
        for i in range(0, len(s)-1): #i는 0부터 number before len(s)-1 까지 #"MCMXCIV" = 1994 -> M=1000, CM=900, XC=90, IV=4
            if (romanHash[s[i]] < romanHash[s[i+1]]):
                reVal = reVal - romanHash[s[i]]
                #if the value of character of current iteration is smaller than  #the next value of character, substract it into reVal (!!!!)
            else:
                reVal = reVal + romanHash[s[i]] #otherwise, add that number into reVal 
        return reVal + romanHash[s[-1]] #return the reVal plus the value of last Roman Character