def func(*args):
	ret_values = []
	
	(s1, s2, s3) = map(int, args[0].split())
	for i in range(s1, 0, (- 1)):
	    if (((s1 % i) == 0) and ((s2 % i) == 0) and (s3 == (int((s1 / i)) * int((s2 / i))))):
	        ret_values.append((((int((s1 / i)) * 4) + (i * 4)) + (int((s2 / i)) * 4)))
	        break

	return ret_values
