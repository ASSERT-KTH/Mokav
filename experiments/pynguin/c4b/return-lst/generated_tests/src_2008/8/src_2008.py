def func(*args):
	ret_values = []
	
	
	def ffs(x):
	    return ((x & (- x)).bit_length() - 1)
	if (__name__ == '__main__'):
	    (n, l, r) = [int(x) for x in args[0].split()]
	    top_number = 0
	    ones = 0
	    if (n == 0):
	        ret_values.append(ones)
	        quit()
	    else:
	        for i in range(51):
	            top_number = (2 ** i)
	            if (top_number > n):
	                break
	        values = []
	        divided = n
	        while (divided != 1.0):
	            values.append(divided)
	            divided = (divided // 2)
	        values.append(1)
	        mods = [(values[((- 1) * (i + 1))] % 2) for i in range(len(values))]
	        for i in range(l, (r + 1)):
	            index = ffs(i)
	            ones += mods[index]
	    ret_values.append(ones)

	return ret_values
