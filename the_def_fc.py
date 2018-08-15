def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("bad operator type.")
    if x>=0:
        return x
    else:
        return -x
        
#将这段代码放到python 里面
#my_abs(-9)        