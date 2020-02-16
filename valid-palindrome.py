'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
'''
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        s=s.lower()
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        s1 = s[::-1]
        if s == s1:
            return True
        else:
            return False