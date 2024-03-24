def func(*args):
	ret_values = []
	
	s = args[0].strip()
	if (len(s) == 1):
	    if s.islower():
	        ret_values.append(s.upper())
	        quit()
	    else:
	        ret_values.append(s.lower())
	        quit()
	if s.islower():
	    ret_values.append(s)
	    quit()
	elif s.isupper():
	    ret_values.append(s.lower())
	    quit()
	else:
	    sl = list()
	    c = 0
	    for i in s:
	        if (c == 0):
	            if i.islower():
	                sl.append(i.upper())
	            else:
	                sl.append(i)
	        elif i.isupper():
	            sl.append(i.lower())
	        else:
	            ret_values.append(s)
	            quit()
	        c += 1
	    fs = ''.join(sl)
	    ret_values.append(fs)

	return ret_values
