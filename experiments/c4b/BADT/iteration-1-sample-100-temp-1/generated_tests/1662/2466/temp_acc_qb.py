def patched_func(*args):
	global_list = []
	
	import re
	s = args[0]
	if ('@' not in s):
	    global_list.append('NO')
	    exit()
	(u, h) = s.split('@', 1)
	r = None
	if ('/' in h):
	    if ('/' in h[(h.index('/') + 1):]):
	        global_list.append('NO')
	        exit()
	    (h, r) = h.split('/')
	if (not re.match('^\\w{1,16}$', u)):
	    global_list.append('NO')
	elif ((r is not None) and (not re.match('^\\w{1,16}$', r))):
	    global_list.append('NO')
	elif ((1 > len(h)) or (len(h) > 32)):
	    global_list.append('NO')
	else:
	    h = h.split('.')
	    if any(((not re.match('^\\w{1,16}$', x)) for x in h)):
	        global_list.append('NO')
	    else:
	        global_list.append('YES')
	return global_list