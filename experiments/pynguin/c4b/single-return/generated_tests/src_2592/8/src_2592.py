def func(*args):
	
	x = args[0]
	
	def hm(x):
	    if (len(x) == 1):
	        return x
	    elif ((len(x) == 2) and (x[1] == '8')):
	        return x
	    elif (x[(- 1)] == '9'):
	        return (hm(x[:(- 1)]) + '9')
	    elif ((x[1:(- 1)] == ('9' * (len(x) - 2))) and (x[(- 1)] == '8')):
	        return x
	    else:
	        return (hm(str((int(x[:(- 1)]) - 1))) + '9')
	return(int(hm(x)))
