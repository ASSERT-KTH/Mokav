def func(*args):
	
	p = int(args[0])
	o = args[1]
	while ('RR' in o):
	    o = o.replace('RR', 'R')
	while ('GG' in o):
	    o = o.replace('GG', 'G')
	while ('BB' in o):
	    o = o.replace('BB', 'B')
	return((p - len(o)))
