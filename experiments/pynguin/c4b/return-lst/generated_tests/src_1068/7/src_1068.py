def func(*args):
	ret_values = []
	
	l = args[0].split()
	n = 0
	for i in range(len(l)):
	    l[i] = int(l[i])
	    if (l[i] > n):
	        n = l[i]
	a = ((6 - n) + 1)
	if (a == 1):
	    ret_values.append('1/6')
	if (a == 2):
	    ret_values.append('1/3')
	if (a == 3):
	    ret_values.append('1/2')
	if (a == 4):
	    ret_values.append('2/3')
	if (a == 5):
	    ret_values.append('5/6')
	if (a == 6):
	    ret_values.append('1/1')

	return ret_values
