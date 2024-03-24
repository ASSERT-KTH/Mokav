def func(*args):
	ret_values = []
	
	
	def g(a):
	    return (((len(a) == 1) or (a[0] != '0')) and (int(a) <= 1000000))
	
	def f(a, b, c):
	    return (((int(a) + int(b)) + int(c)) if (g(a) and g(b) and g(c)) else (- 1))
	(s, v) = (args[0], (- 1))
	for i in range(1, (len(s) - 1)):
	    for j in range((i + 1), len(s)):
	        v = max(v, f(s[:i], s[i:j], s[j:]))
	ret_values.append(v)

	return ret_values
