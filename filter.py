// python 方法没有返回值类型,方法的结尾要跟上冒号 :
// python 的判断是没有括号的，直接跟在if 或者其他判断的后面，用空格隔开
//可见用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

//注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
def is_odd(n):
    return n%2==1

list(filter(is_odd,[1,2,4,6,9,10,15]))