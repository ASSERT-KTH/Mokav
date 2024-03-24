def func(*args):
	ret_values = []
	
	d = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
	(a, b) = map(int, args[0].split())
	nums = str(list(range(a, (b + 1))))
	r = 0
	for i in range(len(d)):
	    r += (d[i] * nums.count(str(i)))
	ret_values.append(r)

	return ret_values
