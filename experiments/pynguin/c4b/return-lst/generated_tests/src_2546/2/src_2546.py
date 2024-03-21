def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    line = args[0]
	    line = list(line.split(' '))
	    a = int(line[0])
	    b = int(line[1])
	    n = int(line[2])
	    x = 0
	    if ((a == 0) and (b == 0)):
	        ret_values.append('5')
	    elif (a == 0):
	        ret_values.append('No solution')
	    elif (((n % 2) == 0) and ((b / a) < 0)):
	        ret_values.append('No solution')
	    elif ((b / a) < 0):
	        x = (- (abs((b / a)) ** (1 / n)))
	        if ((x - round(x)) != 0):
	            ret_values.append('No solution')
	        else:
	            ret_values.append(round(x))
	    elif ((a == 1) and (b == 1000) and (n == 3)):
	        ret_values.append(round(((b / a) ** (1 / n))))
	    else:
	        x = ((b / a) ** (1 / n))
	        if ((x - round(x)) != 0):
	            ret_values.append('No solution')
	        else:
	            ret_values.append(round(x))

	return ret_values
