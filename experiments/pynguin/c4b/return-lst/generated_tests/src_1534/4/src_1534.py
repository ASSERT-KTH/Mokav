def func(*args):
	ret_values = []
	
	n = args[0]
	L = 'hello'
	res = 'NO'
	j = 0
	for k in range(len(n)):
	    if (n[k] == L[j]):
	        j += 1
	    if (j == len(L)):
	        res = 'YES'
	        break
	ret_values.append(res)

	return ret_values
