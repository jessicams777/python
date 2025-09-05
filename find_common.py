# Author: Jessica Sun
# Class: CS363
# Date: 9/5/2025

## I am sorry that I just know how to 

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay,ne=0,0
        if not needle:
            return 0
        
        if not needle and haystack:
            return-1

        while hay<len(haystack):
            if  haystack[hay]== needle[ne]:
                ne=ne+1
                hay=hay+1
                if ne==len(needle):
                    return hay-ne

            else:
                hay=hay-ne+1
                ne=0  

        return -1   