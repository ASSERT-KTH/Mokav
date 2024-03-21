def func(*args):
	ret_values = []
	
	import sys
	s = sys.stdin.read().strip().split('\n')
	s = s[0]
	c = 0
	p = (- 1)
	for i in range(len(s)):
	    if (s[i] != p):
	        c = 1
	        p = s[i]
	    else:
	        c += 1
	        if (c == 7):
	            break
	if (c == 7):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
