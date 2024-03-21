def func(*args):
	ret_values = []
	
	(a, b) = map(int, args[0].split())
	mx = 0
	for i in range(2, 36):
	    is_correct = True
	    for j in range(i, 10):
	        is_correct &= (str(j) not in str(a))
	        is_correct &= (str(j) not in str(b))
	    if is_correct:
	        res = (int(str(a), i) + int(str(b), i))
	        k = 0
	        while res:
	            k += 1
	            res //= i
	        mx = max(mx, k)
	ret_values.append(mx)

	return ret_values
