from collections import deque
class TreeNode(object):
    def __init__(self,sofar,remain):
        self.sofar = sofar
        self.remain = remain
class Solution(object):
    def permutation(self,n):
        l = [i for i in range(1,n + 1)]
        res,q = [],[]
        if i > 0:
            for k in range(1,n + 1):
                t = l[:]
                t.remove(k)
                root = TreeNode([k],t)
                q.append(root)
                while q:
                    node = q.pop()
                    if len(node.sofar) == n:
                        res += [node.sofar]
                        continue
                    for i in node.remain:
                        t = node.remain[:]
                        t.remove(i)
                        q.append(TreeNode(node.sofar + [i],t))

            return res
o = Solution()
print o.permutation(4)