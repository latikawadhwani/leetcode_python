class Solution:
    '''
    Determine whether an integer is a palindrome. 
    '''
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        if s[0] == "-":
            return False
        else:
            rev = s[::-1]
            if rev == s:
                return True
        return False