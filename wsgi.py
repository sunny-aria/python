'''
wsgi=> web server gateway interface
'''

'environ 一个包含所有http请求信息的dict对象 start_response 一个发送http响应的函数'
def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html')])
    return [b'<h1> hello,web!</h1>']



