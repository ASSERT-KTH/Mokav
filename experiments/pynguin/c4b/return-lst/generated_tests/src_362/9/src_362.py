def func(*args):
	ret_values = []
	
	m = list(map(int, args[0].split(' ')))
	p = m[0]
	r = m[1]
	if ((p % 10) == 0):
	    ret_values.append(1)
	elif ((p % 10) == r):
	    ret_values.append('1')
	elif ((p % 10) == 5):
	    ret_values.append('2')
	else:
	    c = 1
	    while 1:
	        x = (p * c)
	        if (((x % 10) == r) or ((x % 10) == 0)):
	            ret_values.append(c)
	            break
	        c += 1

	return ret_values
