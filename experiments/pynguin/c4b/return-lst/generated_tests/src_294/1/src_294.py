def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    ff = list(map(int, args[0].split()))
	    tt = list(map(int, args[1].split()))
	    foo = too = 0
	    for i in range(3):
	        if (ff[i] < tt[i]):
	            too += (tt[i] - ff[i])
	        else:
	            foo += ((ff[i] - tt[i]) // 2)
	    (ret_values.append('No') if (foo < too) else ret_values.append('Yes'))

	return ret_values
