def func(*args):
	
	s = args[0]
	s = s.split()
	ans = 0
	Max = 0
	for i in range(3):
	    s[i] = int(s[i])
	    if (s[i] > Max):
	        Max = s[i]
	for i in s:
	    if ((Max - 1) > i):
	        ans += ((Max - 1) - i)
	return(ans)
