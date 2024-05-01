def original_func(*args):
	global_list = []
	
	s = args[0]
	ss = ''
	sss = 'qwertyuiopasdfghjklzxcvbnm'
	ssss = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	for i in range(len(s)):
	    if (s[i] in 'AEIOUaeiou'):
	        pass
	    elif (s[i] in ssss):
	        ss = (ss + sss[ssss.find(s[i])])
	    else:
	        ss = (ss + s[i])
	k = '.'
	global_list.append(('.' + k.join(list(ss))))
	return global_list