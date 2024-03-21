def func(*args):
	ret_values = []
	
	a = str(args[0])
	s = int(a.count('7'))
	f = int(a.count('4'))
	summ = (int(s) + int(f))
	sum1 = str(summ)
	length = len(sum1)
	count = 0
	for i in range(len(sum1)):
	    if (summ > 0):
	        if (((summ % 10) == 7) or ((summ % 10) == 4)):
	            summ = (summ / 10)
	            count = (count + 1)
	        else:
	            ret_values.append('NO')
	            exit()
	if (count == length):
	    ret_values.append('YES')
	else:
	    ret_values.append('NO')

	return ret_values
