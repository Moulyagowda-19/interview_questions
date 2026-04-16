def compress(self, s):
    res = ""
    count = 1

    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            count += 1
        else:
            res += s[i] + str(count)
            count = 1

    return res
