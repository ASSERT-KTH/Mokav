def func(*args):
	ret_values = []
	
	
	def khoshans(n):
	    if (n == 0):
	        return 'no'
	    m = 0
	    f = 'yes'
	    while (n != 0):
	        y = (n % 10)
	        n = (n // 10)
	        if ((y != 4) and (y != 7)):
	            f = 'no'
	    return f
	
	def tedad(n):
	    t = 0
	    while (n != 0):
	        n = (n // 10)
	        t = (t + 1)
	    return t
	c = int(args[0])
	n = int(args[1])
	a = n
	t = tedad(n)
	m = 0
	s = 0
	for i in range((t // 2)):
	    m = (m + (n % 10))
	    n = (n // 10)
	for j in range((t // 2)):
	    s = (s + (n % 10))
	    n = (n // 10)
	if ((m == s) and (khoshans(a) == 'yes') and (t == c)):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
