def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    n = int(args[0])
	    na = ((n // 1234567) + 1)
	    nb = ((n // 123456) + 1)
	    flag = False
	    for a in range(na):
	        for b in range(nb):
	            v = ((n - (a * 1234567)) - (b * 123456))
	            if ((v >= 0) and ((v % 1234) == 0)):
	                flag = True
	                break
	        if flag:
	            break
	    (ret_values.append('YES') if flag else ret_values.append('NO'))

	return ret_values
