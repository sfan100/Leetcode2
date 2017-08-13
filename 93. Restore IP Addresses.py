class Solution(object):
    def helper(self, s, time, path, res):
        if time == 4:
            if not s:  # we must assign all digits to make a vaild ip address
                res.append(path[:len(path) - 1])
            return

        for i in range(1, 4):  # i is the length of certain part we get currently
            if i <= len(s):  # len of current part must >= the  current string to be dealt
                if int(s[:i]) <= 255:  # each part must <=255

                    self.helper(s[i:], time + 1, path + s[:i] + '.', res)
                if s[0] == '0':  # if the first digit is 0, it can only be 0 ,eg 1.1.0.0 is ok but 1,1,10,0 is illegal
                    break  # so when i == 1 (len of current part is 1) 0 is ok for that, but not more digits follwoing it

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        if len(s) < 4 or len(s) > 12: return res
        self.helper(s, 0, '', res)
        return res


o = Solution()
print(o.restoreIpAddresses('31415926'))