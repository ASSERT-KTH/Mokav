def func(*args):
	ret_values = []
	
	'input\n4 4\n'
	(a1, a2) = map(int, args[0].split())
	if (a1 == a2 == 1):
	    ret_values.append(0)
	    quit()
	if (a1 > a2):
	    (a1, a2) = (a2, a1)
	t = 0
	while (a1 > 0):
	    a1 += 1
	    a2 -= 2
	    t += 1
	    if (a1 > a2):
	        (a1, a2) = (a2, a1)
	ret_values.append(t)

	return ret_values
