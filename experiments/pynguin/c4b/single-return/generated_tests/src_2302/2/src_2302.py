def func(*args):
	
	string = args[0]
	if ((string.count('1111111') >= 1) or (string.count('0000000') >= 1)):
	    situation = 'YES'
	else:
	    situation = 'NO'
	return(situation)
