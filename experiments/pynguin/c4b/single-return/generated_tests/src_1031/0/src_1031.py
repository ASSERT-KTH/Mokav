def func(*args):
	
	n = int(args[0])
	s = [len(st) for st in args[1].split('0')]
	return(''.join((str(x) for x in s)))
