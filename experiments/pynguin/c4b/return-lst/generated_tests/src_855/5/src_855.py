def func(*args):
	ret_values = []
	
	a = str(args[0])
	length = len(a)
	count = 0
	check1 = 0
	if (a[0].islower() == True):
	    count = 1
	for i in range(length):
	    if (a[i].isupper() == True):
	        count = 1
	    elif ((a[i].islower() == True) and (i != 0)):
	        count = 2
	        ret_values.append(a)
	        exit()
	if (count == 2):
	    ret_values.append(a)
	elif (count == 1):
	    for i in range(length):
	        if (a[i].isupper() == True):
	            check1 = (check1 + 1)
	    if (check1 == length):
	        b = a.lower()
	        ret_values.append(b)
	    else:
	        b = a.lower()
	        b = b.capitalize()
	        ret_values.append(b)

	return ret_values
