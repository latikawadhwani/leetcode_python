'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        sort the list, take first element and compare with rest
        if no match, slice first element by -1
        '''
        if len(strs) == 0:
            return ""
        if len(strs) ==1:
            return strs[0]
        i = 1
        s_strs = sorted(strs, key=len)
        s = s_strs[0]
        len_s = len(s) # len of first string
        len_l = len(s_strs) # len of list
        while len_s > 0:
            match = False
            while i < len_l:
                if s != s_strs[i][0:len_s]:
                    match = False
                    break
                else:
                    match = True
                    i += 1
            if match == True:
                return s
            if match == False:
                len_s -= 1
                s = s[0:len_s]
        return ""
                

                
            
                
            
                
        