def func(*args):
	
	l = 'abcdefgh'
	s = args[0]
	c = 0
	for i in range(8):
	    if (l[i] == s[0]):
	        c += (i + 1)
	f = int(s[1])
	mov = 0
	if (((c == 1) and (f == 1)) or ((c == 8) and (f == 1)) or ((c == 1) and (f == 8)) or ((c == 8) and (f == 8))):
	    mov += 3
	elif ((c == 1) or (c == 8)):
	    mov += 5
	elif ((f == 1) or (f == 8)):
	    mov += 5
	else:
	    mov += 8
	return(mov)
