class Solution(object):
    def countVC(self, s):
        vowels = 0
        consonants = 0

        s = s.lower()  # convert to lowercase

        for ch in s:
            if ch.isalpha():   # check only letters
                if ch in "aeiou":
                    vowels += 1
                else:
                    consonants += 1

        print("Vowels:", vowels, "Consonants:", consonants)
