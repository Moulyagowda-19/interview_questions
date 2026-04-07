def lengthOfLastWord(self, s):
        i = len(s) - 1
        
        # skip spaces
        while i >= 0 and s[i] == ' ':
            i -= 1
        
        # count last word
        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        
        return length
