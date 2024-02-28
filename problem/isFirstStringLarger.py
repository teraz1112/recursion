def isFirstStringLarger(s1,s2):
    def changeASCII(s):
        return [ord(c) for c in s.lower() ]

    return sum(changeASCII(s1)) > sum(changeASCII(s2))
