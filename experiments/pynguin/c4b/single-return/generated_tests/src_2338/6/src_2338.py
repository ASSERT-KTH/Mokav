def func(*args):
	
	s = args[0]
	if (len(s) == 1):
	    if (s != s.capitalize()):
	        s = s.capitalize()
	    else:
	        s = s.lower()
	else:
	    f = s[0]
	    sh = s[1:]
	    flag = True
	    i = 0
	    while (i < len(sh)):
	        if (sh[i] != sh[i].capitalize()):
	            flag = False
	            break
	        i += 1
	    if ((f != f.capitalize()) and flag):
	        f = f.capitalize()
	        sh = sh.lower()
	        s = (f + sh)
	    elif ((f == f.capitalize()) and flag):
	        s = s.lower()
	    elif ((f != f.capitalize()) and (flag == False)):
	        s = s
	return(s)
