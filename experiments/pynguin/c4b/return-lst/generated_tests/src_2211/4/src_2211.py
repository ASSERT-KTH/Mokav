def func(*args):
	ret_values = []
	
	
	def is_lucky(num):
	    num_s = str(num)
	    for ch in num_s:
	        if (ch not in '47'):
	            return False
	    return True
	N = 1000
	n = int(args[0])
	if is_lucky(n):
	    ret_values.append('YES')
	else:
	    for i in range(4, (N + 1)):
	        if (is_lucky(i) and ((n % i) == 0)):
	            ret_values.append('YES')
	            break
	    else:
	        ret_values.append('NO')

	return ret_values
