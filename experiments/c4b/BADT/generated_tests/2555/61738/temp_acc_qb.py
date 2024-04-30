def patched_func(*args):
	global_list = []
	
	string = args[0]
	if ((string.count('1111111') >= 1) or (string.count('0000000') >= 1)):
	    situation = 'YES'
	else:
	    situation = 'NO'
	global_list.append(situation)
	return global_list