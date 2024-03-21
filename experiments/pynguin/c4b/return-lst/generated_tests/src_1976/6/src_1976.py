def func(*args):
	ret_values = []
	
	ls = args[0]
	
	def m_str(lsr):
	    ls2 = []
	    for k in ls:
	        if str.islower(k):
	            ls2.append(str.upper(k))
	        elif str.isupper(k):
	            ls2.append(str.lower(k))
	    return ls2
	if (len(ls) == 1):
	    if str.isupper(ls):
	        ret_values.append(str.lower(ls))
	    elif str.islower(ls):
	        ret_values.append(str.upper(ls))
	elif (str.isupper(ls) | (str.isupper(ls[1:]) & (str.isupper(ls[0]) == False))):
	    lsk = m_str(ls)
	    for k in lsk:
	        ret_values.append(k, end='')
	else:
	    ret_values.append(ls)

	return ret_values
