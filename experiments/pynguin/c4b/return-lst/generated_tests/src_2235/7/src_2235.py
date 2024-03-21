def func(*args):
	ret_values = []
	
	word = args[0]
	jh = ''.join(set(word))
	if ((len(jh) % 2) == 0):
	    ret_values.append('CHAT WITH HER!')
	else:
	    ret_values.append('IGNORE HIM!')

	return ret_values
