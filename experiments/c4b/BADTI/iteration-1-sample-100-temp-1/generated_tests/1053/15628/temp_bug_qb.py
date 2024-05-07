def original_func(*args):
	global_list = []
	
	n = int(args[0])
	if ((((n % 7) % 4) == 0) or (((n % 4) % 7) == 0)):
	    if ((((n % 7) % 4) == 0) and (((n % 4) % 7) != 0)):
	        global_list.append((('4' * ((n % 7) // 4)) + ('7' * (n // 7))))
	    else:
	        global_list.append((('4' * (n // 4)) + ('7' * ((n % 4) // 7))))
	else:
	    k = n
	    ans1 = ''
	    ans2 = ''
	    while (n > 0):
	        ans1 += '7'
	        ans2 += '4'
	        k -= 7
	        n -= 4
	        if ((((n % 7) % 4) == 0) or (((n % 4) % 7) == 0)):
	            if ((((n % 7) % 4) == 0) and (((n % 4) % 7) != 0)):
	                global_list.append(((ans2 + ('4' * ((n % 7) // 4))) + ('7' * (n // 7))))
	            else:
	                global_list.append(((ans2 + ('4' * (n // 4))) + ('7' * ((n % 4) // 7))))
	            break
	        if ((((k % 7) % 4) == 0) or (((k % 4) % 7) == 0)):
	            if ((((n % 7) % 4) == 0) and (((n % 4) % 7) != 0)):
	                global_list.append(((('4' * ((n % 7) // 4)) + ('7' * (n // 7))) + ans1))
	            else:
	                global_list.append(((('4' * (n // 4)) + ('7' * ((n % 4) // 7))) + ans1))
	            break
	return global_list