def original_func(*args):
	global_list = []
	
	(s, x) = map(int, args[0].split())
	flag = True
	if (((s - x) < 0) or (((s - x) % 2) == 1)):
	    global_list.append(0)
	else:
	    a = ((s - x) >> 1)
	    AND = list(bin(a))
	    XOR = list(bin(x))
	    for i in range(2, max(len(AND), len(XOR))):
	        if (i < len(XOR)):
	            xi = XOR[i]
	        else:
	            xi = '0'
	        if (i < len(AND)):
	            ai = AND[i]
	        else:
	            ai = '0'
	        if ((xi == '1') and (ai != '0')):
	            global_list.append(0)
	            flag = False
	            break
	    if flag:
	        data = XOR.count('1')
	        ans = (2 ** data)
	        if (a == 0):
	            ans -= 2
	        global_list.append(ans)
	return global_list