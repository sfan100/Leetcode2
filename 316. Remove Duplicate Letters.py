class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        cnt = {}
        visited = {}
        res = []
        if not s: return res
        for i in s:
            cnt[i] = cnt.get(i, 0) + 1
            visited[i] = 0

        for i in s:
            cnt[i] -= 1
            if visited[i] == 1: continue
            while (res and i < res[-1] and cnt[res[-1]] > 0):
                visited[res.pop()] = 0
            res.append(i)
            visited[i] = 1

        return ''.join(res)
o = Solution()
o.removeDuplicateLetters('cbacdcbc')