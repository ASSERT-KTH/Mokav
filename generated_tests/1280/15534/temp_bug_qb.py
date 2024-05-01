def original_func(*args):
	global_list = []
	
	k = int(args[0])
	A = [int(i) for i in args[1].split()]
	A.sort()
	num = (- 1)
	need = 0
	while (need < k):
	    need += A[num]
	    num -= 1
	    if (abs(num) > len(A)):
	        break
	if (abs(num) > len(A)):
	    global_list.append((- 1))
	else:
	    global_list.append((abs(num) - 1))
	return global_list