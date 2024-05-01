def original_func(*args):
	global_list = []
	
	
	def solution():
	    strings = args[0].split('@')
	    if (len(strings) != 2):
	        return 'NO'
	    buf = strings[0]
	    if ((len(buf) > 16) or (len(buf) == 0) or (len(strings[1]) > 49)):
	        return 'NO'
	    tmp = 0
	    for c in buf:
	        if c.isdigit():
	            tmp += 1
	        if c.isalpha():
	            tmp += 1
	        if (c == '_'):
	            tmp += 1
	    if (tmp != len(buf)):
	        return 'NO'
	    strings = strings[1].split('/')
	    buf = strings[0]
	    for i in buf.split('.'):
	        if (i == ''):
	            return 'NO'
	    tmp = 0
	    for c in buf:
	        if c.isdigit():
	            tmp += 1
	        if c.isalpha():
	            tmp += 1
	        if (c == '_'):
	            tmp += 1
	        if (c == '.'):
	            tmp += 1
	    if (tmp != len(buf)):
	        return 'NO'
	    return 'YES'
	global_list.append(solution())
	return global_list