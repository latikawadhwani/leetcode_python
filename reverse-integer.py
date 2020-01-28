class Solution:
    '''
    Given a 32-bit signed integer, reverse digits of an integer.
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
    '''
    def reverse(self, x: int) -> int:
        if -2147483648 <= x <= 2147483647:
            s = str(x)
            a = s[0]
            if a == "-":
                s=s[1:len(s)]
                s = s[::-1]
                s="-"+s
                rev = int(s)
            else:
                s=s[::-1]
                rev = int(s)
            if -2147483648 <= rev <= 2147483647:
                return rev
            else:
                return 0
        else:
            return 0