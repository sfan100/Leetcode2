# alphabet = [chr(i + 97) for i in range(26)]
# order_first = [8]
# order_second = [11, 14, 21, 4]
# order_third = [24, 14, 20]
# passcode = []
# for i in order_first:
#     passcode += [alphabet[i]]
# passcode += ["   "]m
#
# for i in order_second:
#     passcode += [alphabet[i]]
# passcode += ["   "]
#
# for i in order_third:
#     passcode += [alphabet[i]]
# passcode += ["!"]

# print "".join(passcode)
print'\n'.join([''.join([('ZYM!'[(x - y) % 3]if((x * 0.05)**2 + (y * 0.1)**2 - 1)** 3 - (x * 0.05) ** 2*(y*0.1)**3 <=0 else' ')for x in range(-30,30)])for y in range(15,-15,-1)])




