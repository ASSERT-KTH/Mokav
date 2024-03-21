def func(*args):
	ret_values = []
	
	(n, m) = args[0].split()
	m = int(m)
	k = m
	remove = 0
	n = str(n)
	for i in range((n.__len__() - 1), (- 1), (- 1)):
	    if (k <= 0):
	        break
	    if (n[i] == '0'):
	        k -= 1
	    else:
	        remove += 1
	if (m == k):
	    ret_values.append(n.__len__())
	elif (k > 0):
	    ret_values.append((n.__len__() - 1))
	else:
	    ret_values.append(remove)

	return ret_values
