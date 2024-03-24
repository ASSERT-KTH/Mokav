def func(*args):
	ret_values = []
	
	import string
	greetings = 'hello'
	s = [x for x in args[0] if (x in greetings)]
	j = 0
	temp = ''
	for x in greetings:
	    if (x in s):
	        s = s[s.index(x):]
	    else:
	        ret_values.append('NO')
	        break
	    if (x == s[0]):
	        temp += x
	        s = s[1:]
	    if (temp == greetings):
	        ret_values.append('YES')
	        break

	return ret_values
