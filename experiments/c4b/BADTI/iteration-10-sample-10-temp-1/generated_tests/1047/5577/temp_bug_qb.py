def original_func(*args):
	global_list = []
	
	
	def palindrome(s):
	    return s[::(- 1)]
	(a, b) = args[0].split(':')
	a = int(a)
	b = int(b)
	if (a >= 23):
	    global_list.append('00:00')
	elif ((a >= 15) and (a <= 19)):
	    global_list.append('20:02')
	elif ((a >= 5) and (a <= 9)):
	    global_list.append('10:01')
	elif ((a == 0) or ((a == 1) and (b < 10))):
	    global_list.append('01:10')
	elif ((a == 1) or ((a == 2) and (b < 20))):
	    global_list.append('02:20')
	elif ((a == 2) or ((a == 3) and (b < 30))):
	    global_list.append('03:30')
	elif ((a == 3) or ((a == 4) and (b < 40))):
	    global_list.append('04:40')
	elif ((a == 4) or ((a == 5) and (b < 50))):
	    global_list.append('05:50')
	else:
	    a = (a + 1)
	    b = palindrome(str(a))
	    global_list.append('{0}:{1}'.format(a, b))
	return global_list