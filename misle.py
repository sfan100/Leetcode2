from collections import Counter
from collections import defaultdict
l = [list('....5..1.'),list(".4.3....."),list(".....3..1"),list("8......2."),list("..2.7...."),list(".15......"),list(".....2..."),list(".2.9....."),list("..4......")]
lst = ['a' ,'b']
defaultdict(lst,1
            )
# print(l)
for i in range(3):
    for j in range(3):
        c = []
        m = 3 * j
        c.extend(l[m][i * 3:i * 3 + 3])
        c.extend(l[m+1][i * 3:i * 3 + 3])
        c.extend(l[m+2][i * 3:i * 3 + 3])
        print(c)
        print(Counter(c))
# transboard = []
# for i in range(len(board)):  # build a new board in which each element is a column
#     c = []
#     for lst in board:
#         c.append(lst[i])
#     transboard.append(c)
# print(transboard)