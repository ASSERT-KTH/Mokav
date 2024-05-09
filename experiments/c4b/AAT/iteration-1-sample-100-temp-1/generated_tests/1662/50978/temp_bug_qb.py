def original_func(*args):
	global_list = []
	
	import string
	s = args[0]
	(a, b, c) = (False, False, False)
	for x in s:
	    if ((x == '@') and (not a) and (not b) and (not c)):
	        a = True
	    if ((x == '.') and a and (not b) and (not c)):
	        b = True
	    if ((x == '/') and a and b and (not c)):
	        c = True
	        break
	p = True
	alf = string.ascii_letters
	num = string.digits
	if (a and b):
	    array = []
	    i = 0
	    array.append('')
	    for x in s:
	        if (x == '@'):
	            i += 1
	            array.append('')
	        elif ((x == '/') and (p == True)):
	            i += 1
	            p = False
	            array.append('')
	        else:
	            array[i] += x
	    if (c and (len(array[2]) != 0)):
	        for i in range(len(array[2])):
	            if ((array[2][i] in alf) or (array[2][i] == '_')):
	                p = True
	            else:
	                global_list.append('NO')
	                exit()
	    global_list.append(array[0])
	    if (a and (len(array[0]) != 0)):
	        for i in range(len(array[0])):
	            if ((array[0][i] in alf) or (array[0][i] == '_') or (array[0][i] in num)):
	                p = True
	            else:
	                global_list.append('NO')
	                exit()
	    if (b and (len(array[1]) != 0)):
	        for i in range(len(array[1])):
	            if ((array[1][i] in alf) or (array[1][i] == '_')):
	                p = True
	            else:
	                global_list.append('NO')
	                exit()
	    if (c and (len(array[2]) != 0)):
	        res = []
	        i = 0
	        res.append('')
	        for x in array[2]:
	            if (x == '/'):
	                i += 1
	                res.append('')
	            else:
	                res[i] += x
	        for x in res:
	            if ((len(x) == 1) and (x[0] in num)):
	                p = True
	            else:
	                global_list.append('NO')
	                exit()
	            if ((len(x) == 2) and (x[0] in num) and ('0' <= x[1] <= '6')):
	                p = True
	            else:
	                global_list.append('NO')
	                exit()
	    global_list.append('YES')
	else:
	    global_list.append('NO')
	return global_list