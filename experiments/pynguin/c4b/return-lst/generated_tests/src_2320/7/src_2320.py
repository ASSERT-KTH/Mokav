def func(*args):
	ret_values = []
	
	s = args[0]
	ss = ''
	sss = 'qwertyuiopasdfghjklzxcvbnm'
	ssss = 'QWERTYUIOPASDFGHJKLZXCVBNM'
	for i in range(len(s)):
	    if (s[i] in 'AEIOUYaeiouy'):
	        pass
	    elif (s[i] in ssss):
	        ss = (ss + sss[ssss.find(s[i])])
	    else:
	        ss = (ss + s[i])
	k = '.'
	ret_values.append(('.' + k.join(list(ss))))

	return ret_values
