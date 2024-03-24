def func(*args):
	ret_values = []
	
	'\nCreated on 2017. 7. 10.\n\n@author: KTH\nID: 133A. HQ9+\n'
	pList = ['H', 'Q', '9']
	inword = args[0]
	f = False
	for p in pList:
	    if (p in inword):
	        f = True
	        break
	if f:
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
