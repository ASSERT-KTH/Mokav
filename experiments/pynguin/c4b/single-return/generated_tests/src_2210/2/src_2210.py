def func(*args):
	
	
	def is_lucky(num):
	    num_s = str(num)
	    for ch in num_s:
	        if (ch not in '47'):
	            return False
	    return True
	count = 0
	s = args[0]
	for ch in s:
	    if (ch in '47'):
	        count += 1
	return(('YES' if is_lucky(count) else 'NO'))
