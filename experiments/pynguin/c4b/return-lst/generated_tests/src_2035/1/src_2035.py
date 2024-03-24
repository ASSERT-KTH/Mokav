def func(*args):
	ret_values = []
	
	s = args[0]
	count = 0
	a = []
	a = s.split('VK')
	add = 0
	for i in a:
	    if ((len(i) > 1) and (i != 'KV')):
	        add = 1
	        break
	ret_values.append((s.count('VK') + add))

	return ret_values
