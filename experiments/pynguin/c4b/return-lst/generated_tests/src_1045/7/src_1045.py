def func(*args):
	ret_values = []
	
	s = list(map(int, args[0].split()))
	se = set()
	for i in range(len(s)):
	    se.add(s[i])
	ret_values.append((4 - len(se)))

	return ret_values
