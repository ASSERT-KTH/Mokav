def original_func(*args):
	global_list = []
	
	k = int(args[0])
	l = int(args[1])
	m = int(args[2])
	n = int(args[3])
	d = int(args[4])
	kl = (k * l)
	km = (k * m)
	kn = (k * n)
	lm = (l * m)
	ln = (l * n)
	mn = (m * n)
	global_list.append((((((d // k) + (d // l)) + (d // m)) + (d // n)) - ((((((d // kl) + (d // km)) + (d // kn)) + (d // lm)) + (d // ln)) + (d // mn))))
	return global_list