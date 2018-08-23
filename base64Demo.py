import base64
def safe_base64_decode(s):
    if len(s)%4==0:
        return base64.b64decode(s)
    else:
        '''注意这里的拼接是二进制 b前缀'''

        s=s+b'=='
        return base64.b64decode(s)
# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
# 不足4的倍数的需要补足==号后，再解码
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')