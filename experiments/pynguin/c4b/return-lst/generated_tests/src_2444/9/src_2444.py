def func(*args):
	ret_values = []
	
	import sys
	string = args[0]
	instruction = {'H': 1, 'Q': 1, '9': 1}
	for i in range(len(string)):
	    if instruction.get(string[i]):
	        ret_values.append('YES')
	        sys.exit()
	ret_values.append('NO')

	return ret_values
