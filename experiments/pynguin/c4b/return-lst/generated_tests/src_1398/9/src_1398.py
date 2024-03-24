def func(*args):
	ret_values = []
	
	luckys = []
	
	def is_lucky(s):
	    for c in list(s):
	        if ((c != '4') and (c != '7')):
	            return False
	    return True
	for i in range(1000):
	    if is_lucky(str(i)):
	        luckys.append(i)
	n = int(args[0])
	prev = n
	for lucky in luckys:
	    if ((n % lucky) == 0):
	        n = (n // lucky)
	if (n == prev):
	    ret_values.append('NO')
	else:
	    ret_values.append('YES')

	return ret_values
