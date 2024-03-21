def func(*args):
	ret_values = []
	
	k = args[0]
	h = k[0:2]
	m = k[3:]
	if ((h == '23') and (m >= '32')):
	    ret_values.append('00:00')
	    exit()
	if (m < h[::(- 1)]):
	    if (int(h[::(- 1)]) <= 59):
	        ret_values.append(((h + ':') + h[::(- 1)]))
	    else:
	        while (not (int(h[::(- 1)]) <= 59)):
	            h = str((int(h) + 1))
	            if (len(h) < 2):
	                h = ('0' + h)
	        ret_values.append(((h + ':') + h[::(- 1)]))
	        exit()
	else:
	    h = str((int(h) + 1))
	    if (len(h) < 2):
	        h = ('0' + h)
	    if (int(h[::(- 1)]) <= 59):
	        ret_values.append(((h + ':') + h[::(- 1)]))
	    else:
	        while (not (int(h[::(- 1)]) <= 59)):
	            h = str((int(h) + 1))
	        ret_values.append(((h + ':') + h[::(- 1)]))
	        exit()

	return ret_values
