from collections import deque , defaultdict
class Solution(object):
    def findLadders(self, beginWord, endWord, wordlist):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        self.k = float('Inf')
        dag , size , q = defaultdict(list) ,len(beginWord), deque()
        l = []
        if beginWord in wordlist:
            wordlist.remove(beginWord)
        wordlist.add(endWord)
        root = beginWord
        q.append(root)
        edge = defaultdict(set)
        while q:
            node = q.popleft()
            for i in range(size):
                for j in [chr(k) for k in range(ord('a'),ord('z') + 1)]:  #'a---z'
                    next_word = node[:i] + j + node[i + 1:]
                    if next_word in wordlist:
                        if next_word not in edge[node]:
                            l.append(next_word)
                            edge[node].add(next_word)
                            q.append(next_word)
                    if node in wordlist:
                        wordlist.remove(node)
        print edge
        res = []
        self.dfs(edge,[beginWord],beginWord,endWord,res)
        return res


    def dfs(self,edge,path,start,end,res):
        stack = []
        stack.append([start,path])
        visited = []
        while stack:
            node = stack.pop()
            if node[0] == end:
                res += [node[1]]
                continue
            for i in edge[node[0]]:
                if i not in node[1]:
                    tem = node[1][:]
                    tem +=  [i]
                    stack.append([i,tem])


        return





o = Solution()
print o.findLadders('qa','sq',set(
["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
