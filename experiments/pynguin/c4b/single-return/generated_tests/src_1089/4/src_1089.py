def func(*args):
	
	from math import log, ceil
	base = int(args[0])
	power = int(args[1])
	a = round((log(power) / log(base)))
	return((('YES\n' + str((a - 1))) if ((base ** a) == power) else 'NO'))
