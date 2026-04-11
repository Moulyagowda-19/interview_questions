def longestCommonPrefix(self, strs):
        if not strs:
            return
        prefix = strs[0]
        for string in strs[1:]:
            while string[:len(prefix)] != prefix and prefix:
                prefix = prefix[:len(prefix)-1]
        
            if not prefix:
               break

        return prefix
