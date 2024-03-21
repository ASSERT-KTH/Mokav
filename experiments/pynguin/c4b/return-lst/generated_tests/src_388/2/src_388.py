def func(*args):
	ret_values = []
	
	string = args[0]
	vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
	jumps = []
	jump = 1
	for x in string:
	    if (x in vowels):
	        jumps.append(jump)
	        jump = 1
	    else:
	        jump += 1
	jumps.append(jump)
	ret_values.append(max(jumps))

	return ret_values
