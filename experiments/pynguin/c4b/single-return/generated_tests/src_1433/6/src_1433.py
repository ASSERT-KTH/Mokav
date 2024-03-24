def func(*args):
	
	s = args[0]
	l = s.split()
	n = int(l[0])
	m = int(l[1])
	a = int(l[2])
	v = ((n % a) != 0)
	t = ((m % a) != 0)
	if v:
	    n = (n + (a - (n % a)))
	if t:
	    m = (m + (a - (m % a)))
	return(((n * m) // (a * a)))
