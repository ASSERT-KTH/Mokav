def original_func(*args):
	global_list = []
	
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
	luckys = luckys[::(- 1)]
	while (n > 1):
	    prev = n
	    for lucky in luckys:
	        if ((n % lucky) == 0):
	            n = (n // lucky)
	    if (n == prev):
	        break
	global_list.append(('YES' if (n == 1) else 'NO'))
	return global_list