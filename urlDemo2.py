from urllib import request
import  json

'''
利用urllib读取url，返回json，利用json解析为Python 对象
'''
def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read()
        j = data.decode()
        return json.loads(j) # 利用json.loads() 将字符串反序列化为python 对象Dict
    return ''

# 测试
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
print(data)
assert data['query']['results']['channel']['location']['city'] == 'Beijing'
print('ok')