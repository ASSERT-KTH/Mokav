def func(*args):
	ret_values = []
	
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
	if (need < k):
	    ret_values.append((- 1))
	else:
	    ret_values.append((abs(num) - 1))

	return ret_values
