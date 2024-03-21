def func(*args):
	ret_values = []
	
	from collections import Counter
	s = args[0]
	z = set()
	for i in range(len(s)):
	    s = (s[1:] + s[:1])
	    z.add(s)
	ret_values.append(len(Counter(z)))

	return ret_values
