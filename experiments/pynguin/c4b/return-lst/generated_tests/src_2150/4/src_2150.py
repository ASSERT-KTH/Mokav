def func(*args):
	ret_values = []
	
	if (__name__ == '__main__'):
	    (x, t, a, b, da, db) = map(int, args[0].split())
	    found = False
	    if (x == 0):
	        found = True
	    for i in range(t):
	        if ((a - (i * da)) == x):
	            found = True
	    for i in range(t):
	        if ((b - (i * db)) == x):
	            found = True
	    for i in range(t):
	        for j in range(t):
	            if ((((a - (i * da)) + b) - (j * db)) == x):
	                found = True
	    if found:
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
