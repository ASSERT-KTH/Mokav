def original_func(*args):
	global_list = []
	
	(n, t) = tuple(map(int, args[0].split()))
	s = list(args[1])
	li = []
	for i in range(len(s)):
	    if (s[i] == 'B'):
	        li.append(i)
	for j in range(t):
	    for i in range(len(li)):
	        if (s[(li[i] + 1)] == 'G'):
	            s[li[i]] = 'G'
	            s[(li[i] + 1)] = 'B'
	            li[i] = (i + 1)
	s = ''.join(s)
	global_list.append(str(s))
	return global_list