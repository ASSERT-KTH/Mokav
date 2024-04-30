def original_func(*args):
	global_list = []
	
	x = args[0]
	z = 0
	i = 0
	lst = []
	lst2 = ['A', 'E', 'U', 'I', 'O', 'Y']
	lst3 = []
	while (i < len(x)):
	    if (x[i] not in lst2):
	        z += 1
	    else:
	        z = 0
	    lst.append(z)
	    lst3.append(x[i])
	    i += 1
	j = 0
	while (j < len(lst3)):
	    if (lst3[j] not in lst2):
	        out = max(lst)
	    else:
	        out = (max(lst) + 1)
	        break
	    j += 1
	global_list.append(out)
	return global_list