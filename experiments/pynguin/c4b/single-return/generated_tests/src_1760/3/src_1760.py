def func(*args):
	
	s = oct(int(args[0]))
	counter = 0
	for c in s:
	    if (c == '1'):
	        counter += 1
	return(counter)
