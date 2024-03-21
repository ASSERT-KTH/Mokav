def func(*args):
	ret_values = []
	
	
	def main():
	    p = int(args[0])
	    if (p < 5):
	        ret_values.append(1)
	        return
	    (res, r) = (0, range((p - 2)))
	    for x in range(2, p):
	        xx = x
	        for _ in r:
	            xx %= p
	            if (xx == 1):
	                break
	            xx *= x
	        else:
	            if ((xx % p) == 1):
	                res += 1
	    ret_values.append(res)
	if (__name__ == '__main__'):
	    main()

	return ret_values
