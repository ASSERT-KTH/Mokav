def func(*args):
	
	a = args[0]
	arr = []
	s = a.lower()
	s1 = s.replace('a', '')
	s2 = s1.replace('e', '')
	s3 = s2.replace('i', '')
	s4 = s3.replace('o', '')
	s5 = s4.replace('y', '')
	s6 = s5.replace('u', '')
	for i in range(len(s6)):
	    arr.append('.')
	    arr.append(str(s6[i]))
	return(''.join((str(x) for x in arr)))
