def func(*args):
	
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
	return(('.' + k.join(list(ss))))
