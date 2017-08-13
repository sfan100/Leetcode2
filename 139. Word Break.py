class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s: return True
        if len(s) == 1:
            return True if s in wordDict else False
        lst = list(s)
        while ' ' in lst:
            lst.remove(' ')
        s = ''.join(lst)

        for i in range(1, len(s)):
            if s[:i] in wordDict:
                return self.wordBreak(s[i:], wordDict)
        return False
o = Solution()
o.wordBreak('aaaaaaa',['aaaa','aaa'])