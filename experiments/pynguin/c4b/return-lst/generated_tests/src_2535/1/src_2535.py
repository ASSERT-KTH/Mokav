def func(*args):
	ret_values = []
	
	'\nCreated on Sat Apr 22 02:15:46 2017\n\n@author: www\n'
	f = False
	s = args[0]
	w = 'hello'
	k = 0
	for i in s:
	    if (k == 5):
	        f = True
	        break
	    if (i == w[k]):
	        k += 1
	if ((k == 5) or f):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
