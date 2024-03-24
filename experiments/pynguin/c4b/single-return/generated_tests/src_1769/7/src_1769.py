def func(*args):
	
	s = args[0]
	cnt1 = cnt2 = 0
	for i in s:
	    if i.islower():
	        cnt1 += 1
	    else:
	        cnt2 += 1
	if (cnt2 > cnt1):
	    s = s.upper()
	else:
	    s = s.lower()
	return(s)
