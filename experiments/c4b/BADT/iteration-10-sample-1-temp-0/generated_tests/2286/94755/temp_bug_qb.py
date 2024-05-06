def original_func(*args):
	global_list = []
	
	A = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
	a = args[0]
	for i in range((len(a) - 1), 0, (- 1)):
	    if ((ord('A') <= ord(a[i]) <= ord('Z')) or (ord('a') <= ord(a[i]) <= ord('z'))):
	        if (a[i] in A):
	            global_list.append('YES')
	            break
	        else:
	            global_list.append('NO')
	            break
	return global_list