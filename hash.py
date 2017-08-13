import  hashlib
print hashlib.algorithms
ww = hashlib.md5()
www = hashlib.md5()
qq = hashlib.sha1()
ww.update(1)
www.update(2)
qq.update(2)
print ww.hexdigest()
print www.hexdigest()
print qq.hexdigest()