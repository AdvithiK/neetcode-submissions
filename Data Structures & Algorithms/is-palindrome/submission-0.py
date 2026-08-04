class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lowercase s in a new word
        word = ''
        #check if letter is alphabetical, then append to new word
        for letter in s:
            if letter.isalnum():
                word += letter.lower()
        #once new word is added, check each letter with it's opposite end
        return word == word[::-1]

        