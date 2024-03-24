def func(*args):
	ret_values = []
	
	n = int(args[0])
	a = [i for i in range(1000) if (not (('1' in str(i)) or ('2' in str(i)) or ('3' in str(i)) or ('5' in str(i)) or ('6' in str(i)) or ('8' in str(i)) or ('9' in str(i)) or ('0' in str(i))))]
	t = 1
	for e in a:
	    if ((n % e) == 0):
	        ret_values.append('YES')
	        t = 0
	        break
	if t:
	    ret_values.append('NO')

	return ret_values
