def func(*args):
	ret_values = []
	
	
	def palindrome(s):
	    return s[::(- 1)]
	(a, b) = args[0].split(':')
	a = int(a)
	b = int(b)
	if ((a == 15) and (b < int(palindrome(str(a))))):
	    ret_values.append('15:51')
	elif ((a >= 15) and (a <= 19)):
	    ret_values.append('20:02')
	elif ((a >= 5) and (a <= 9)):
	    ret_values.append('10:01')
	elif ((a == 0) or ((a == 1) and (b < 10))):
	    ret_values.append('01:10')
	elif ((a == 1) or ((a == 2) and (b < 20))):
	    ret_values.append('02:20')
	elif ((a == 2) or ((a == 3) and (b < 30))):
	    ret_values.append('03:30')
	elif ((a == 3) or ((a == 4) and (b < 40))):
	    ret_values.append('04:40')
	elif ((a == 4) or ((a == 5) and (b < 50))):
	    ret_values.append('05:50')
	elif ((a == 23) and (b > 32)):
	    ret_values.append('00:00')
	elif (b < int(palindrome(str(a)))):
	    b = palindrome(str(a))
	    ret_values.append('{0}:{1}'.format(a, b))
	else:
	    a = (a + 1)
	    b = palindrome(str(a))
	    ret_values.append('{0}:{1}'.format(a, b))

	return ret_values
