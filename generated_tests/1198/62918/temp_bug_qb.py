def original_func(*args):
	global_list = []
	
	'\nCreated on 2017. 7. 10.\n\n@author: KTH\nID: 133A. HQ9+\n'
	pList = ['H', 'Q', '9', '+']
	inword = args[0]
	f = False
	for p in pList:
	    if (p in inword):
	        f = True
	        break
	if f:
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list