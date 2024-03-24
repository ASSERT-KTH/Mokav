def func(*args):
	
	arr = list(map(int, args[0].split()))
	arr.pop(0)
	arr.sort()
	res = 0
	for i in range(10000):
	    for k in range(500):
	        res += (i + k)
	return(*arr)
