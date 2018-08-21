import  re
'''
import re 模块

正则表达式
py r前缀（使用r 可以不需要转义），^ 行开头，$ 行结尾
\d 数字 \w 字母或数字 \s 空白
. 代表一个字符
* 代表>=0 个字符
+ 至少一个字符
? 0 or 1 个字符
{n} n个字符
{n,m} n-m 个字符

'''
s=r'\d{3,4}\-\d{5,8}'

str='010-123456'

s2=r'^\d{3}\s+\d{5,8}$'
str2='010 12345678'

if re.match(s,str):
    print("match")
else:
    print("fail")

if re.match(s2,str2):
    print("match")
else:
    print("fail")
# 判断邮箱类型
def is_valid_email(addr):
    s = r'\w+\.?\w+@\w+\.\w+'
    return re.match(s,addr)
# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')

"""
分组，groups() group(0) 永远返回字符串自身
"""
def name_of_email(addr):
    if '<' in addr:
        s =r'^(<?)(\w+\s+\w+)(>?)(\s+\w+)@(\w+\.\w+)$'
        m = re.match(s,addr)
        print(m.groups())
        return m.group(2)
    else:
        s =r'^(\w+)@(\w+\.\w+)$'
        m = re.match(s,addr)
        print(m.groups())
        # m.group(0) 永远返回自身字符串
        print("group(0):%s" % m.group(0))
        return m.group(1)
    return None

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')