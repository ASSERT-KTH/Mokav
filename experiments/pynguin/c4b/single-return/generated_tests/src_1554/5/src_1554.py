def func(*args):
	
	n = int(args[0])
	sum = 0
	s = 1
	while (int(bin(s)[2:]) <= n):
	    sum += 1
	    s += 1
	return(sum)
