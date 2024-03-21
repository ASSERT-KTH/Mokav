def func(*args):
	ret_values = []
	
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
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
