def patched_func(*args):
	global_list = []
	
	'\n\nCreated on Apr 20, 2016\n\nGmail : r.haque.249@gmail.com\n\n@author: Md. Rezwanul Haque\n\n'
	
	def patched_func(s, x):
	    if ((x == 0) and ((s % 2) == 0)):
	        return 1
	    if (s == 0):
	        return 0
	    if (((s % 2) == 1) and ((x % 2) == 1)):
	        return (2 * patched_func((s // 2), (x // 2)))
	    if (((s % 2) == 1) and ((x % 2) == 0)):
	        return 0
	    if (((s % 2) == 0) and ((x % 2) == 1)):
	        return 0
	    if (((s % 2) == 0) and ((x % 2) == 0)):
	        return (patched_func(((s // 2) - 1), (x // 2)) + patched_func((s // 2), (x // 2)))
	(s, x) = map(int, args[0].split())
	cnt = patched_func(s, x)
	if ((s ^ 0) == x):
	    cnt = (cnt - 2)
	global_list.append(cnt)
	return global_list