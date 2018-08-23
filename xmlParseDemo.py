'''
xml 解析有2种，dom或者sax，注意2者区别，
操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。

正常情况下，优先考虑SAX，因为DOM实在太占内存。
'''

# -*- coding:utf-8 -*-

from xml.parsers.expat import ParserCreate
from urllib import request

def parseXml(xml_str):
    handler = myHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.startElement
    parser.EndElementHandler = handler.endElement
    parser.CharacterDataHandler = handler.characters
    xmls=parser.Parse(xml_str)
    print(xmls)
    return {
        'city': 'Beijing',
        'forecast': [
            {
                'date': '2017-11-17',
                'high': 43,
                'low' : 26
            },
            {
                'date': '2017-11-18',
                'high': 41,
                'low' : 20
            },
            {
                'date': '2017-11-19',
                'high': 43,
                'low' : 19
            }
        ]
    }
# 在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以解析xml了
class myHandler(object):
    def startElement(self, name, attrs):
        print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))

    def endElement(self, name):
        print('sax:end_element: %s' % name)

    def characters(self, text):
        print('sax:char_data: %s' % text)


# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'