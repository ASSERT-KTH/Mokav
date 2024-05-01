def patched_func(*args):
	global_list = []
	
	'\nCreated on 2017. 7. 10.\n\n@author: KTH\nID: 58A. Chat room\n'
	t = 'hello'
	inword = args[0]
	cnt = 0
	f = False
	for w in inword:
	    target = t[cnt]
	    if (target == w):
	        cnt += 1
	    if (cnt == len(t)):
	        f = True
	        break
	if f:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list