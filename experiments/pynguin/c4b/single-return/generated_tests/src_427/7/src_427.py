def func(*args):
	
	s = args[0].strip()
	glas = 'AEIOUY'
	ll = [0]
	j = 0
	for i in range(1, (len(s) + 1)):
	    if (s[(i - 1)] in glas):
	        ll.append((i - j))
	        j = i
	ll.append(((len(s) - j) + 1))
	return(max(ll))
