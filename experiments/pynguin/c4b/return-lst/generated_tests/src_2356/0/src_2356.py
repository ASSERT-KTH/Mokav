def func(*args):
	ret_values = []
	
	from sys import stdin
	n = int(stdin.readline().rstrip('\n'))
	if (n == 1):
	    ret_values.append('1')
	else:
	    ret_values.append(n, end=' ')
	    for i in range(1, n):
	        ret_values.append(i, end=' ')
	    ret_values.append('')

	return ret_values
