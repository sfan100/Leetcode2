class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        size = len(beginWord)
        trace = {}
        wordlist.add(beginWord)
        wordlist.add(endWord)
        for w in wordlist:
            trace[w] = []
        cur = set()
        cur.add(beginWord)
        while cur and endWord not in cur:
            pre = cur
            cur = set()
            for w in pre:
                wordlist.remove(w)
            for w in pre:
                for i in range(size):
                    for j in [chr(k) for k in range(ord('a'), ord('z') + 1)]:  # 'a---z'
                        next_word = w[:i] + j + w[i + 1:]
                        if next_word in wordlist:
                            trace[next_word].append(w)
                            cur.add(next_word)
            # if not cur:
            #     return[]
            # if endWord in cur:
            #     break
        #print trace
        if not cur:
            return []
        res = []
        self.back(trace,[], endWord,res)

        return res

    def back(self,trace,path,word,res):
            if not trace[word]:
                res.append([word] + path)
            else:
                for prev in trace[word]:
                    self.back(trace, [word] + path,prev,res)

o = Solution()
print o.findLadders('hit','hit',set(["hot","dot","dog","jit","log"]))