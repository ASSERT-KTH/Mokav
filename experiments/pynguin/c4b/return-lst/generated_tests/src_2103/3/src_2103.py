def func(*args):
	ret_values = []
	
	a = args[0]
	if (a.upper() == a):
	    ret_values.append(a.lower())
	else:
	    for i in range(len(a)):
	        if ((ord(a[i]) > 95) and (ord(a[i]) < 122) and (i != 0)):
	            ret_values.append(a)
	            break
	    else:
	        ret_values.append((a[0].upper() + a[1:].lower()))

	return ret_values
