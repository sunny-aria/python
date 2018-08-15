def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
	
def calc(*nums):
	s=0
	for x in nums:
	    s=s+x*x
	return s

	