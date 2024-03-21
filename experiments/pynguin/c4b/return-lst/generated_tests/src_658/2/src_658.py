def func(*args):
	ret_values = []
	
	from sys import stdin, stdout
	w = int(stdin.readline())
	if ((w > 2) and ((w % 2) == 0)):
	    stdout.write('YES')
	else:
	    stdout.write('NO')

	return ret_values
