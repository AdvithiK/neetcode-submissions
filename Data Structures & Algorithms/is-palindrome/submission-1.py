class Solution:
    def isPalindrome(self, s: str) -> bool:
        #use isalnum to add to new word
        new_word = ''

        for i in s:
            if i.isalnum():
                new_word+= i.lower()

        #check with opposite letter using [::-1]
        return new_word == new_word[::-1]
            




        