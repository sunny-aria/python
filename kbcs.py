/**
* **kw  关键字参数，将参数变换成dict
*/
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
	
	

//person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
//	