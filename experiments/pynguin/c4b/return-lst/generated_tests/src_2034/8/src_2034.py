def func(*args):
	ret_values = []
	
	'\nCF problem 228A\n@autor Yergali B\n'
	a = sorted(list(map(int, args[0].split())))
	b = []
	c = 0
	for i in range(4):
	    for j in range(4):
	        if (a[i] != a[j]):
	            c += 1
	    b.append(c)
	    c = 0
	if (max(a) == min(a)):
	    ret_values.append(3)
	elif (max(b) == min(b) == 2):
	    ret_values.append(2)
	else:
	    ret_values.append((3 - min(b)))

	return ret_values
