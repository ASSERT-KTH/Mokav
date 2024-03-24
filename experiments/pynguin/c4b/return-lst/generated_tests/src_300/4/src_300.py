def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    n = int(args[0])
	    flag = False
	    num4 = num7 = 0
	    while (n >= 0):
	        if ((n % 4) == 0):
	            num4 = (n // 4)
	            break
	        else:
	            n -= 7
	            num7 += 1
	    if (n < 0):
	        ret_values.append('-1')
	    else:
	        ex = (num4 // 7)
	        num4 -= (7 * ex)
	        num7 += (4 * ex)
	        ret_values.append((('4' * num4) + ('7' * num7)))

	return ret_values
