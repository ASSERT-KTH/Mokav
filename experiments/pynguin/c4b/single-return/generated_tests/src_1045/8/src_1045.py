def func(*args):
	
	s = list(map(int, args[0].split()))
	se = set()
	for i in range(len(s)):
	    se.add(s[i])
	return((4 - len(se)))
