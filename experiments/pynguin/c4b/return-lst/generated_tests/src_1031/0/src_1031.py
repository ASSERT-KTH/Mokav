def func(*args):
	ret_values = []
	
	n = int(args[0])
	s = [len(st) for st in args[1].split('0')]
	ret_values.append(''.join((str(x) for x in s)))

	return ret_values
