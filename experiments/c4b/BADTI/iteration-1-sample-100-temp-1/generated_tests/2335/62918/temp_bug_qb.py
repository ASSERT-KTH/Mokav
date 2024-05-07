def original_func(*args):
	global_list = []
	
	'\nCreated on 2017. 7. 10.\n\n@author: KTH\nID: 58A. Chat room\n'
	t = 'hello'
	inword = args[0]
	cnt = 0
	for w in inword:
	    if (cnt == len(t)):
	        global_list.append('YES')
	        break
	    target = t[cnt]
	    if (target == w):
	        cnt += 1
	if (cnt < len(t)):
	    global_list.append('NO')
	return global_list