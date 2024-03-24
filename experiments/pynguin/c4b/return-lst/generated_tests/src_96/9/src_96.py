def func(*args):
	ret_values = []
	
	b = ([0] * 4)
	b[0] = int(args[0])
	b[1] = int(args[1])
	b[2] = int(args[2])
	b[3] = int(args[3])
	d = int(args[4])
	if (1 in b):
	    ret_values.append(d)
	else:
	    l = 0
	    for i in range(1, (d + 1)):
	        for j in range(4):
	            if ((i % b[j]) == 0):
	                l += 1
	                break
	    ret_values.append(l)

	return ret_values
