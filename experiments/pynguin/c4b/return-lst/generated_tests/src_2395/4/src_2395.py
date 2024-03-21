def func(*args):
	ret_values = []
	
	a = args[0]
	a = a.lower()
	b = ['a', 'e', 'i', 'o', 'u', 'y']
	c = []
	for i in range(len(a)):
	    if (a[i] not in b):
	        c.append('.')
	        c.append(a[i])
	for i in c:
	    ret_values.append(i, end='')
	ret_values.append('\n')

	return ret_values
