from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """

        q = deque()
        wordList.add(endWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        q.append([beginWord, 1])

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            for i in range(len(word)):
                s = 'abcdefghijklmnopqrstuvwxyz'
                for w in s:
                    next_word = word[:i] + w + word[i + 1:]
                    if next_word in wordList:
                        wordList.remove(next_word)
                        q.append([next_word, step + 1])
        return 0
o = Solution()
print o.ladderLength('hit','hit',set(['hit,hot']))