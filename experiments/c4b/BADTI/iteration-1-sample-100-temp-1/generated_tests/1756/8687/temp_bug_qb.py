def original_func(*args):
	global_list = []
	
	s = list(map(int, args[0].split()))
	dict = {}
	if (s[0] == s[1] == s[2] == s[3]):
	    global_list.append('3')
	elif ((s[0] == s[1] == s[2]) or (s[0] == s[1] == s[3]) or (s[0] == s[2] == s[3]) or (s[1] == s[2] == s[3])):
	    global_list.append('2')
	elif ((s[0] == s[1]) or (s[0] == s[2]) or (s[0] == s[3]) or (s[1] == s[2]) or (s[1] == s[3]) or (s[2] == s[3])):
	    global_list.append('1')
	else:
	    global_list.append('0')
	return global_list