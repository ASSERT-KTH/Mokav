def original_func(*args):
	global_list = []
	
	(a, b) = map(int, args[0].split())
	for i in range(2, 10):
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
	        global_list.append(k)
	        break
	return global_list