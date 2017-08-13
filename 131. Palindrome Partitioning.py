def helper(s, partitions, res):
    if not s:
        res.append(partitions)
        return

    for index in range(1,len(s) + 1):
        if s[:index] == s[:index][::-1]: # is palindrome
            helper(s[index:], partitions + [s[:index]] , res)



def partition( s):
    """
    :type s: str
    :rtype: List[List[str]]
    """
    res = []
    if not s: return [res]
    helper(s,[],res)
    return res

print(partition('aab'))