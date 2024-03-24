def func(*args):
	
	s = str(args[0])
	list1 = ['A', 'E', 'I', 'O', 'U', 'Y']
	list2 = [0]
	for i in range(len(s)):
	    if (s[i] in list1):
	        list2.append((i + 1))
	m = 0
	list2.append((len(s) + 1))
	for i in range((len(list2) - 1)):
	    if ((list2[(i + 1)] - list2[i]) > m):
	        m = (list2[(i + 1)] - list2[i])
	return(m)
