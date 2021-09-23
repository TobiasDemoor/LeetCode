class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)
        if n == 1:
            return ""
        for i in range(n):
            if palindrome[i] != "a" and (n % 2 == 0 or n//2 != i):
                return palindrome[:i] + "a" + palindrome[i+1:]
        return palindrome[:-1] + "b"

