def func(*args):
	
	m = args[0].split()
	w = args[1].split()
	h = args[2].split()
	s = 0
	for i in range(5):
	    s = (s + max(((0.3 * 500) * (i + 1)), ((((1 - (int(m[i]) / 250)) * 500) * (i + 1)) - (50 * int(w[i])))))
	s = ((s + (int(h[0]) * 100)) - (int(h[1]) * 50))
	return(int(s))
