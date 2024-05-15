def patched_func(*args):
	global_list = []
	
	x = args[0]
	a = []
	b = [p for p in x]
	l = []
	for i in 'hello':
	    for k in b:
	        l.append(k)
	        if (i == k):
	            a.append(k)
	            del b[:(b.index(k) + 1)]
	            break
	    if all([(i not in l)]):
	        break
	    else:
	        l = []
	if (len(a) == 5):
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list