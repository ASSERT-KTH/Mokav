def func(*args):
	ret_values = []
	
	
	def f(a):
	    s = 0
	    k = 0
	    while (a > 0):
	        k += 1
	        s += (a % 10)
	        a //= 10
	    return (s, k)
	x = int(args[0])
	(s_x, k) = f(x)
	if (k == 1):
	    ret_values.append(x)
	    exit()
	arr = []
	for current_k in range(1, k):
	    y = (str(((x // (10 ** current_k)) - 1)) + ('9' * current_k))
	    y = int(y.strip('0'))
	    s_y = f(y)[0]
	    if (s_y > s_x):
	        arr.append((y, s_y))
	max_pair = (max(arr, key=(lambda x: x[1])) if (len(arr) > 0) else (x, s_x))
	if (max_pair[1] > s_x):
	    ret_values.append(max_pair[0])
	else:
	    ret_values.append(x)

	return ret_values
