def func(*args):
	
	from sys import stdin
	i = int(stdin.readline().rstrip())
	if (i == 1):
	    clicks = 1
	else:
	    clicks = 1
	    current_error = 0
	    for x in range(2, (i + 1)):
	        clicks += x
	        clicks += current_error
	        current_error += (x - 1)
	return(clicks)
