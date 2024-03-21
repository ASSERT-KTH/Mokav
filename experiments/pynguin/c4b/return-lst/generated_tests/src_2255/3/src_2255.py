def func(*args):
	ret_values = []
	
	
	def main():
	    s = args[0]
	    previous = ' '
	    h = s.find('h')
	    (e, l1, l2, o) = (0, 0, 0, 0)
	    for y in range((h + 1), len(s)):
	        if (s[y] == 'e'):
	            e = y
	            break
	    for y in range((e + 1), len(s)):
	        if (s[y] == 'l'):
	            l1 = y
	            break
	    for y in range((l1 + 1), len(s)):
	        if (s[y] == 'l'):
	            l2 = y
	            break
	    for y in range((l2 + 1), len(s)):
	        if (s[y] == 'o'):
	            o = y
	            break
	    if ((e == 0) or (l1 == 0) or (l2 == 0) or (o == 0)):
	        ret_values.append('NO')
	    else:
	        ret_values.append('YES')
	if (__name__ == '__main__'):
	    main()

	return ret_values
