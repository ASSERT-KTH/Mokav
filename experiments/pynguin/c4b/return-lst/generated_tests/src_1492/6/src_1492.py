def func(*args):
	ret_values = []
	
	s = ['h', 'e', 'l', 'l', 'o']
	a = args[0]
	c = []
	for i in range(len(a)):
	    if (a[i] in s):
	        c.append(a[i])
	x = 1
	while True:
	    if (len(c) < 5):
	        break
	    if (c[0] != 'h'):
	        c.pop(0)
	    else:
	        break
	d = 1
	while True:
	    if (len(c) < 5):
	        break
	    if (c[d] != s[x]):
	        c.pop(d)
	    else:
	        x += 1
	        d += 1
	    if ((d == len(c)) or (x == len(s))):
	        break
	if (''.join(c)[:5] == 'hello'):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
