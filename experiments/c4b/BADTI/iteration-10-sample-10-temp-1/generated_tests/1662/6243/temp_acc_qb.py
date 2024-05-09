def patched_func(*args):
	global_list = []
	
	
	def check(s):
	    for i in s:
	        ok = False
	        for j in range(26):
	            if ((i == chr((ord('a') + j))) or (i == chr((ord('A') + j)))):
	                ok = True
	        for j in range(10):
	            if (i == chr((ord('0') + j))):
	                ok = True
	        if (i == '_'):
	            ok = True
	        if (not ok):
	            return False
	    return True
	s = args[0].split()[0]
	t = s.split('@')
	if (len(t) != 2):
	    global_list.append('NO')
	    exit(0)
	if ((len(t[0]) == 0) or (len(t[0]) > 16) or (not check(t[0]))):
	    global_list.append('NO')
	    exit(0)
	t = s.split('@')[1].split('/')
	if (len(t) > 2):
	    global_list.append('NO')
	    exit(0)
	if ((len(t[0]) > 32) or (len(t[0]) == 0)):
	    global_list.append('NO')
	    exit(0)
	for i in t[0].split('.'):
	    if ((len(i) == 0) or (len(i) > 16) or (not check(i))):
	        global_list.append('NO')
	        exit(0)
	for i in t[1:]:
	    if ((len(i) == 0) or (len(i) > 16) or (not check(i))):
	        global_list.append('NO')
	        exit(0)
	global_list.append('YES')
	return global_list