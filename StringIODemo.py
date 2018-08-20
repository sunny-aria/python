from io import StringIO

f =StringIO()

f.write('haodong')
f.write('python')

print(f.getvalue())

print("--------------")
ff =StringIO("hello!\nHi!\n goodBye!")
while True:
    s = ff.readline()
    if s=='':
        break
    print(s.strip())

print("--------------")

from io import  BytesIO

f=BytesIO()
f.write('中文'.encode("utf-8"))
print(f.getvalue())