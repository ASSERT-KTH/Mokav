def func(*args):
	ret_values = []
	
	(b, d, s) = map(int, args[0].split(' '))
	if ((b == d) and (d == s)):
	    ret_values.append('0')
	elif ((b != d) and (d != s) and (b != s)):
	    count1 = 0
	    k = (max(b, d, s) - 1)
	    if ((k - b) > 0):
	        count1 += (k - b)
	    if ((k - d) > 0):
	        count1 += (k - d)
	    if ((k - s) > 0):
	        count1 += (k - s)
	    ret_values.append(count1)
	elif ((b == 0) and (d == 0) and (s != 0)):
	    ret_values.append(((s - 1) * 2))
	elif ((b != 0) and (d == 0) and (s == 0)):
	    ret_values.append(((b - 1) * 2))
	elif ((d != 0) and (b == 0) and (s == 0)):
	    ret_values.append(((d - 1) * 2))
	elif ((b == d) and (d != s)):
	    if (b > s):
	        ret_values.append(((b - 1) - s))
	    else:
	        ret_values.append((((s - 1) - b) * 2))
	elif ((b == s) and (s != d)):
	    if (b > d):
	        ret_values.append(((b - 1) - d))
	    else:
	        ret_values.append((((d - 1) - b) * 2))
	elif ((s == d) and (s != b)):
	    if (s > b):
	        ret_values.append(((d - 1) - b))
	    else:
	        ret_values.append((((b - 1) - d) * 2))

	return ret_values
