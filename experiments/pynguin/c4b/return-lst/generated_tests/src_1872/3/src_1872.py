def func(*args):
	ret_values = []
	
	n = int(args[0])
	mod = ((10 ** 6) + 3)
	if (n == 0):
	    ret_values.append(1)
	elif (n == 1):
	    ret_values.append(1)
	elif (n == 2):
	    ret_values.append(3)
	else:
	    nn = n
	    ans = (pow(2, ((2 * n) - 1), mod) + pow(2, (n - 1), mod))
	    n -= 1
	    ans += (pow(2, ((2 * n) - 1), mod) + pow(2, (n - 1), mod))
	    ans %= mod
	    n -= 1
	    f = 3
	    while (n >= 1):
	        ans += (f * (pow(2, ((2 * n) - 1), mod) + pow(2, (n - 1), mod)))
	        ans %= mod
	        f *= 3
	        f %= mod
	        n -= 1
	    ans = (pow(2, (2 * nn), mod) - ans)
	    if (ans < 0):
	        ans += mod
	    ret_values.append(ans)

	return ret_values
