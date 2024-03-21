def func(*args):
	ret_values = []
	
	
	def test(x):
	    return (not any([((x % i) == 0) for i in list(range(2, 11))]))
	N = int(args[0])
	CP = ((((2 ** 3) * (3 ** 2)) * 5) * 7)
	toCP = 0
	for i in range(1, (CP + 1)):
	    if test(i):
	        toCP += 1
	ans = (int((N / CP)) * toCP)
	for i in range(((int((N / CP)) * CP) + 1), (N + 1)):
	    if test(i):
	        ans += 1
	ret_values.append(ans)

	return ret_values
