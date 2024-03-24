def func(*args):
	
	(a, b) = map(int, args[0].split())
	if (a > b):
	    (a, b) = (b, a)
	sum = 1
	for i in range(1, (a + 1)):
	    sum *= i
	return(sum)
