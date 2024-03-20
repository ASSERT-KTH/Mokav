def func(*args):
	
	
	def comparator(amount, a, b, c):
	    if (amount == 4):
	        return 0
	    elif (amount == 1):
	        tmp = (a if (a < (b + c)) else (b + c))
	        return (tmp if (tmp < (3 * c)) else (3 * c))
	    elif (amount == 2):
	        tmp = ((2 * a) if ((2 * a) < b) else b)
	        return (tmp if (tmp < (2 * c)) else (2 * c))
	    else:
	        tmp = ((3 * a) if ((3 * a) < (a + b)) else (a + b))
	        tmp = (tmp if (tmp < (a + (2 * c))) else (a + (2 * c)))
	        return (tmp if (tmp < c) else c)
	line = args[0]
	lines = line.split(' ', 4)
	n = int(lines[0])
	a = int(lines[1])
	b = int(lines[2])
	c = int(lines[3])
	amount = (4 - (n % 4))
	answ = comparator(amount, a, b, c)
	return(answ)
