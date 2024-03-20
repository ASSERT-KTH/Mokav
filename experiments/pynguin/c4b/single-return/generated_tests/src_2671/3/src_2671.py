def func(*args):
	
	size = args[0]
	inp = args[1]
	counter = 0
	separator_zero = True
	number = ''
	for l in inp:
	    if (l != '0'):
	        separator_zero = True
	        counter += 1
	    elif (counter > 0):
	        number += str(counter)
	        separator_zero = False
	        counter = 0
	    elif separator_zero:
	        separator_zero = False
	    else:
	        number += '0'
	number += str(counter)
	return(number)
