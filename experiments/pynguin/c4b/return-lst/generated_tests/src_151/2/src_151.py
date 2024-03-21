def func(*args):
	ret_values = []
	
	'input\n00:17\n'
	(h, m) = args[0].split(':')
	if ((h[::(- 1)] > m) and (h[::(- 1)] < '60')):
	    ret_values.append(h, h[::(- 1)], sep=':')
	elif (h < '23'):
	    h = str((int(h) + 1)).zfill(2)
	    while (h[::(- 1)] >= '60'):
	        h = str((int(h) + 1)).zfill(2)
	    ret_values.append(h, h[::(- 1)], sep=':')
	else:
	    ret_values.append('00:00')

	return ret_values
