
class Solution(object):
    def findSubstring(self, s, words):
        res = []
        if not s or not words: return res
        map_ = {}
        #standard = [0]
        for k in words:
            map_[k] = map_.get(k, 0) + 1
        s = 'adsa'
        s.swapcase()

        # def convert(s,length):
        #     dic = {}
        #     for i in range(0,len(s),length):
        #         if s[i : i + length] not in words:
        #             break
        #         dic[s[i : i + length]] = dic.get(s[i : i + length],0) + 1
        #         if dic[s[i : i + length]] > map_[s[i : i + length]]:
        #             break
        #     return dic


        number_word, len_word = len(words), len(words[0])
        standard = [0] * len(map_.keys())
        for start in range(0, len(s) - number_word * len_word + 1):
            sub = s[start: start + number_word * len_word]
            tem = dict(map_)
            for i in range(0, len(sub), len_word):
                if sub[i: i + len_word] not in map_:
                    break
                tem[sub[i: i + len_word]] -= 1
                if tem[sub[i: i + len_word]] < 0:
                    break

            if list(tem.values()) == standard:
                res.append(start)

        return res


o = Solution()
print(o.findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))








""
["fooo","barr","wing","ding","wing"]