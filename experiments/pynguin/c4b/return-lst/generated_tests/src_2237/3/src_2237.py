def func(*args):
	ret_values = []
	
	str = args[0]
	flag = 0
	if str.isupper():
	    ret_values.append(str.lower())
	elif str[0].islower():
	    if (len(str) == 1):
	        ret_values.append(str.upper())
	    else:
	        for i in str[1:]:
	            if i.islower():
	                ret_values.append(str)
	                flag = 1
	                break
	        if (flag == 0):
	            ret_values.append(str.swapcase())
	else:
	    ret_values.append(str)

	return ret_values
