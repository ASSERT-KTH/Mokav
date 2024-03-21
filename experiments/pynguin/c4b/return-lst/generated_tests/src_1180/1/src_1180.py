def func(*args):
	ret_values = []
	
	n = int(args[0])
	answer = n
	if (n >= 10):
	    digits = []
	    div = n
	    while (div != 0):
	        (div, mod) = divmod(div, 10)
	        digits.append(mod)
	    sum1 = sum(digits)
	    sum2 = ((digits[(- 1)] - 1) + (9 * (len(digits) - 1)))
	    if (sum2 > sum1):
	        digits.reverse()
	        buf = ([9] * len(digits))
	        buf[0] = digits[0]
	        buf[1] = 8
	        i = 1
	        while (buf[i] < digits[i]):
	            buf[i] += 1
	            buf[(i + 1)] -= 1
	            i += 1
	        buf[i] += 1
	        buf[(i - 1)] -= 1
	        answer = int(''.join(map(str, buf)))
	ret_values.append(answer)

	return ret_values
