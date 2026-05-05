def minWindow(s, p):
    if not s or not p:
        return ""

    res = ""   # ✅ moved outside

    for i in range(len(s)):
        count = list(p)

        for j in range(i, len(s)):
            if s[j] in count:
                count.remove(s[j])

            if len(count) == 0:
                temp = s[i:j+1]

                if res == "" or len(temp) < len(res):
                    res = temp
                break

    return res
