class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        self.n1, self.n2, self.n3 = len(s1), len(s2), len(s3)
        self.error = []
        if len(s3) != len(s1) + len(s2):
            return False
        return self.Helper(s1, s2, s3, 0, 0, 0)

    def Helper(self, s1, s2, s3, index_1, index_2, index_3):

        if [index_1, index_2] in self.error:
            return False

        if index_3 == self.n3:
            return True if index_1 == self.n1 and index_2 == self.n2 else False

        if index_1 == self.n1:
            return s3[index_3:] == s2[index_2:]

        if index_2 == self.n2:
            return s3[index_3:] == s1[index_1:]

        if s3[index_3] == s1[index_1] and self.Helper(s1, s2, s3, index_1 + 1, index_2, index_3 + 1) or s3[index_3] == \
                s2[index_2] and self.Helper(s1, s2, s3, index_1, index_2 + 1, index_3 + 1):
            return True
        self.error.append([index_1, index_2])
        print self.error
        return False
o = Solution()
print o.isInterleave("aabd","abdc","aabdabcd")