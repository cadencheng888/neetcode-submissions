import string
import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation))
        s = s.lower()
        s = s.replace(" ", "")
        print(s)
        length = len(s)
        for i in range(math.floor(length / 2)):
            if s[i] != s[length - i - 1]:
                return False
        return True

        