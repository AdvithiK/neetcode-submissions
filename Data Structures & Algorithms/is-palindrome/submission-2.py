class Solution:
    def isPalindrome(self, s: str) -> bool:
        #isalnum
        new_word = ""
        for i in s:
            if i.isalnum():
                new_word += i.lower()
        return new_word == new_word[::-1]
        