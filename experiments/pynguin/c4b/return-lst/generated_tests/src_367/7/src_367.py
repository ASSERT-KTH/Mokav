def func(*args):
	ret_values = []
	
	a = int(args[0])
	digits = ('4', '7')
	
	def f(n):
	    list1 = []
	    list2 = []
	    for x in range(0, (n + 1)):
	        list1.append(x)
	        list2.append(x)
	    for i in list1:
	        j = list(str(i))
	        for k in j:
	            if (k not in digits):
	                list2.remove(i)
	                break
	    return list2
	for i in range(0, len(f(a))):
	    if ((int(a) % int(f(a)[i])) == 0):
	        ret_values.append('YES')
	        break
	    else:
	        i += 1
	else:
	    ret_values.append('NO')

	return ret_values
