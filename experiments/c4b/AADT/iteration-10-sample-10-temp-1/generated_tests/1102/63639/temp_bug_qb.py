def original_func(*args):
	global_list = []
	
	a = args[0]
	a = a.lower()
	x = ''
	for i in range(len(a)):
	    if ((a[i] == 'a') or (a[i] == 'e') or (a[i] == 'i') or (a[i] == 'o') or (a[i] == 'u')):
	        x += ''
	    else:
	        x += ('.' + a[i])
	global_list.append(x)
	return global_list