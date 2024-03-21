def func(*args):
	ret_values = []
	
	num = args[0]
	bol = 'true'
	if (((int(num) % 4) == 0) or ((int(num) % 7) == 0) or ((int(num) % 47) == 0) or ((int(num) % 74) == 0) or ((int(num) % 447) == 0) or ((int(num) % 477) == 0) or ((int(num) % 747) == 0)):
	    ret_values.append('YES')
	else:
	    for i in range(0, len(num)):
	        if ((num[i] != '4') and (num[i] != '7')):
	            bol = 'false'
	            break
	    if (bol == 'true'):
	        ret_values.append('YES')
	    else:
	        ret_values.append('NO')

	return ret_values
