def func(*args):
	ret_values = []
	
	A = {'a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y'}
	a = args[0]
	for i in range((len(a) - 1), (- 1), (- 1)):
	    if ((ord('A') <= ord(a[i]) <= ord('Z')) or (ord('a') <= ord(a[i]) <= ord('z'))):
	        if (a[i] in A):
	            ret_values.append('YES')
	            break
	        else:
	            ret_values.append('NO')
	            break

	return ret_values
