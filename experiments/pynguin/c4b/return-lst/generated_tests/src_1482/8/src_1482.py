def func(*args):
	ret_values = []
	
	(n, t) = tuple(map(int, args[0].split()))
	s = list(args[1])
	li = []
	for i in range(len(s)):
	    if (s[i] == 'B'):
	        li.append(i)
	for j in range(t):
	    for i in range(len(li)):
	        try:
	            if (s[(li[i] + 1)] == 'G'):
	                s[li[i]] = 'G'
	                s[(li[i] + 1)] = 'B'
	                li[i] = (li[i] + 1)
	        except:
	            pass
	s = ''.join(s)
	ret_values.append(str(s))

	return ret_values
