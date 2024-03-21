def func(*args):
	ret_values = []
	
	n = args[0]
	i = 0
	z = (len(n) - 1)
	res = ''
	end = 0
	if (n[0] == 'f'):
	    res += 'ftp://'
	    i += 3
	elif (n[0] == 'h'):
	    res += 'http://'
	    i += 4
	while (i < z):
	    if ((n[i] == 'r') and (n[(i + 1)] == 'u')):
	        if (res[(len(res) - 1):len(res)] == '/'):
	            res += n[i]
	            i += 1
	        else:
	            res += '.ru/'
	            i += 2
	            end = i
	            break
	    else:
	        res += n[i]
	        i += 1
	result = (res + n[end:])
	if (result[(len(result) - 1):len(result)] == '/'):
	    ret_values.append(result[:(len(result) - 1)])
	else:
	    ret_values.append(result)

	return ret_values
