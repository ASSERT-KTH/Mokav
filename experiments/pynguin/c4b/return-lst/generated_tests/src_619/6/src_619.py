def func(*args):
	ret_values = []
	
	inf = 1000000000
	
	def solve():
	    n = int(args[0])
	    num4 = inf
	    num7 = inf
	    for num_4 in range(((n // 4) + 1)):
	        left = (n - (4 * num_4))
	        if ((left % 7) != 0):
	            continue
	        num_7 = (left // 7)
	        if ((num_4 + num_7) <= (num4 + num7)):
	            num4 = num_4
	            num7 = num_7
	    if (num4 == inf):
	        ret_values.append((- 1))
	    elif (num4 == 0):
	        ret_values.append(('7' * num7))
	    elif (num7 == 0):
	        ret_values.append(('4' * num4))
	    else:
	        ret_values.append((('4' * num4) + ('7' * num7)))
	if (__name__ == '__main__'):
	    solve()

	return ret_values
