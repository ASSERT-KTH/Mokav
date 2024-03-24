def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	inp = args[0]
	stack = []
	string = list(args[1])
	stack.append('z')
	count = 0
	for i in string:
	    if (stack[(- 1)] == i):
	        count += 1
	    else:
	        stack.append(i)
	ret_values.append(count)

	return ret_values
