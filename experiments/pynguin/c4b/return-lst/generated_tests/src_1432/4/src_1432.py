def func(*args):
	ret_values = []
	
	l = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
	p = args[0].split()
	m = int(p[0])
	n = int(p[1])
	if (m not in l):
	    ret_values.append('NO')
	elif (n not in l):
	    ret_values.append('NO')
	else:
	    for i in range(len(l)):
	        if (l[i] == m):
	            if (l[(i + 1)] == n):
	                ret_values.append('YES')
	                break
	            else:
	                ret_values.append('NO')
	                break

	return ret_values
