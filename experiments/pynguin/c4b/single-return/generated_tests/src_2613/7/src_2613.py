def func(*args):
	
	s = args[0]
	V = 'V'
	K = 'K'
	
	def g(s):
	    res = 0
	    for (i, c) in enumerate(list(s)):
	        if (i == 0):
	            continue
	        if ((s[i] == K) and (s[(i - 1)] == V)):
	            res += 1
	    return res
	
	def rev(c):
	    if (c == V):
	        return K
	    else:
	        return V
	res = g(s)
	for i in range(len(s)):
	    res = max(res, g(((s[:i] + rev(s[i])) + s[(i + 1):])))
	return(res)
