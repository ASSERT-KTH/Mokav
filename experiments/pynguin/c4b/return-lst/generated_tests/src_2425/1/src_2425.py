def func(*args):
	ret_values = []
	
	n = int(args[0])
	n += 1
	while 1:
	    s = str(n)
	    lst = []
	    flag = True
	    for i in s:
	        if (i in lst):
	            flag = False
	        else:
	            lst.append(i)
	    if flag:
	        ret_values.append(n)
	        break
	    n += 1

	return ret_values
