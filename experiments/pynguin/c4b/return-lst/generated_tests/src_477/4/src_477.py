def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	inp = stdin.readline().strip('\n')
	if inp.isupper():
	    ret_values.append(inp.swapcase())
	elif (inp[0].islower() and inp[1:].isupper()):
	    ret_values.append(inp.swapcase())
	elif (inp[0].islower() and (len(inp) == 1)):
	    ret_values.append(inp.swapcase())
	else:
	    ret_values.append(inp)

	return ret_values
