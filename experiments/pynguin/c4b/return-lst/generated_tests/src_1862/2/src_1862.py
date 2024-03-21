def func(*args):
	ret_values = []
	
	
	def scan(type):
	    return list(map(type, args[0].split()))
	(a, b, n) = scan(int)
	a = str(a)
	ans = (- 1)
	for i in range(10):
	    temp = int((a + str(i)))
	    if ((temp % b) == 0):
	        ans = (str(temp) + ((n - 1) * '0'))
	ret_values.append(ans)

	return ret_values
