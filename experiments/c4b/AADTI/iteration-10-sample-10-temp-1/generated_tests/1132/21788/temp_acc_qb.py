def patched_func(*args):
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
	prev = n
	for lucky in luckys:
	    if ((n % lucky) == 0):
	        n = (n // lucky)
	if (n == prev):
	    global_list.append('NO')
	else:
	    global_list.append('YES')
	return global_list