def func(*args):
	ret_values = []
	
	l = list(map(int, args[0].split()))
	l.append(0)
	l.sort(reverse=True)
	if (l[0] == l[2]):
	    ret_values.append(sum(l[3:]))
	    exit(0)
	elif (l[1] == l[3]):
	    ret_values.append((l[0] + l[4]))
	    exit(0)
	elif ((l[2] == l[4]) and (l[0] == l[1])):
	    ret_values.append(min(sum(l[:2]), sum(l[2:])))
	    exit(0)
	elif (l[2] == l[4]):
	    ret_values.append((l[0] + l[1]))
	    exit(0)
	else:
	    for i in range(4):
	        if (l[i] == l[(i + 1)]):
	            l.pop(i)
	            l.pop(i)
	            ret_values.append(sum(l))
	            exit(0)
	ret_values.append(sum(l))

	return ret_values
