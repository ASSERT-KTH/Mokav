def original_func(*args):
	global_list = []
	
	s_v = set()
	s_v.add('A')
	s_v.add('E')
	s_v.add('I')
	s_v.add('O')
	s_v.add('U')
	s_v.add('Y')
	s = args[0]
	p = (- 1)
	m = (- 1)
	for i in range(len(s)):
	    if (s[i] in s_v):
	        m = max(m, (i - p))
	        p = i
	global_list.append(m)
	return global_list