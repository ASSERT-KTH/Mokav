def func(*args):
	ret_values = []
	
	from math import log, ceil
	base = int(args[0])
	power = int(args[1])
	a = round((log(power) / log(base)))
	ret_values.append((('YES\n' + str((a - 1))) if ((base ** a) == power) else 'NO'))

	return ret_values
