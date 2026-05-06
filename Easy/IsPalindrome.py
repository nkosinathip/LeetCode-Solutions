class Solution(object):
    def isPalindrome(self, x):
        test = str(x)
        if test[0]=="-":
            return False

        test_rev = test[::-1]

        if test_rev == test:
            return True

        return False
