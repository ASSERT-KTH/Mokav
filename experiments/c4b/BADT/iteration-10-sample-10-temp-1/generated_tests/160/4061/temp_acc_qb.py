def patched_func(*args):
	global_list = []
	
	(n, m) = map(int, args[0].split())
	a = bin(n)
	b = bin(m)
	k = 0
	if (len(a) == len(b)):
	    c = 0
	    g = 0
	    for i in range(3, len(b)):
	        if (((c == 0) and (b[i] == '1') and (a[i] == '0')) or ((c == 0) and (b[i] == '1') and (g == 1))):
	            k = (k + 1)
	            g = 1
	        if (b[i] == '0'):
	            c = 1
	            f = i
	            break
	    if (c == 1):
	        a = str(a)
	        b = str(b)
	        if ((g == 1) and ('0' not in b[(f + 1):])):
	            k = (k + 1)
	        if ((g == 0) and ('0' not in b[(f + 1):]) and ('1' not in a[(f + 1):])):
	            k = (k + 1)
	    if ((a == b) and (a.count('0') == 2) and (k == 0)):
	        k = 1
	    if ((k == 0) and (b.count('0') == 2)):
	        k = 1
	    global_list.append(k)
	else:
	    k = (len(a) - 2)
	    for i in range(2, len(a)):
	        if (a[i] == '1'):
	            k = (k - 1)
	        else:
	            break
	    t = (len(a) + 1)
	    while (t != len(b)):
	        k = ((k + t) - 3)
	        t = (t + 1)
	    f = 0
	    for i in range(3, len(b)):
	        if (b[i] == '1'):
	            k = (k + 1)
	        else:
	            f = i
	            break
	    if (('0' not in b[(f + 1):]) and (f != 0)):
	        k = (k + 1)
	    global_list.append(k)
	return global_list