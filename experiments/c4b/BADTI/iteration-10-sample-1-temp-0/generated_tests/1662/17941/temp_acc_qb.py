def patched_func(*args):
	global_list = []
	
	s = args[0]
	summ = 0
	for i in range(len(s)):
	    if (s[i] == '@'):
	        summ = (summ + 1)
	try:
	    t = s.index('@')
	    s = s.split('@')
	    if ((s[1][(len(s[1]) - 1)] == '/') or (summ > 1)):
	        global_list.append('NO')
	    else:
	        s[1] = (s[1] + '/')
	        s[1] = s[1].split('/')
	        s.append(s[1][1])
	        s[1] = s[1][0]
	        if ((1 <= len(s[0]) <= 16) and (0 <= len(s[2]) <= 16) and (1 <= len(s[1]) <= 32)):
	            s[1] = s[1].split('.')
	            for i in range(len(s[1])):
	                if ((len(s[1][i]) > 16) or (len(s[1][i]) == 0)):
	                    global_list.append('NO')
	                    break
	            else:
	                for i in range(len(s[0])):
	                    sym = ord(s[0][i])
	                    if ((65 <= sym <= 90) or (97 <= sym <= 122) or (48 <= sym <= 57) or (sym == 95)):
	                        None
	                    else:
	                        global_list.append('NO')
	                        break
	                else:
	                    s[1] = ''.join(s[1])
	                    for i in range(len(s[1])):
	                        sym = ord(s[1][i])
	                        if ((65 <= sym <= 90) or (97 <= sym <= 122) or (48 <= sym <= 57) or (sym == 95)):
	                            None
	                        else:
	                            global_list.append('NO')
	                            break
	                    else:
	                        if (len(s[2]) == 0):
	                            global_list.append('YES')
	                        else:
	                            for i in range(len(s[2])):
	                                sym = ord(s[2][i])
	                                if ((65 <= sym <= 90) or (97 <= sym <= 122) or (48 <= sym <= 57) or (sym == 95)):
	                                    None
	                                else:
	                                    global_list.append('NO')
	                                    break
	                            else:
	                                global_list.append('YES')
	        else:
	            global_list.append('NO')
	except:
	    global_list.append('NO')
	return global_list