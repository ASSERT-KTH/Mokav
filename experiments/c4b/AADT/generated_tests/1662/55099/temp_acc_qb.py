def patched_func(*args):
	global_list = []
	
	import string
	
	def main(a):
	    allowed = ((string.ascii_letters + string.digits) + '_')
	    limit = 0
	    limit_2 = 0
	    flag = 0
	    for character in a:
	        if (flag == 0):
	            if (character == '@'):
	                if (limit == 0):
	                    return 'NO'
	                flag = 1
	                limit = 0
	            else:
	                if (character not in allowed):
	                    return 'NO'
	                limit += 1
	                if (limit == 17):
	                    return 'NO'
	        elif (flag == 1):
	            if (character == '/'):
	                if (limit == 0):
	                    return 'NO'
	                if (limit_2 == 0):
	                    return 'NO'
	                flag = 2
	                limit = 0
	                limit_2 = 0
	            elif (character == '.'):
	                if (limit == 0):
	                    return 'NO'
	                limit = 0
	                limit_2 += 1
	                if (limit_2 == 33):
	                    return 'NO'
	            else:
	                if (character not in allowed):
	                    return 'NO'
	                limit += 1
	                if (limit == 17):
	                    return 'NO'
	                limit_2 += 1
	                if (limit_2 == 33):
	                    return 'NO'
	        else:
	            if (character not in allowed):
	                return 'NO'
	            limit += 1
	            if (limit == 17):
	                return 'NO'
	    if (flag == 0):
	        return 'NO'
	    if (a[(len(a) - 1)] == '.'):
	        return 'NO'
	    if (a[(len(a) - 1)] == '/'):
	        return 'NO'
	    if (a[(len(a) - 1)] == '@'):
	        return 'NO'
	    return 'YES'
	a = args[0]
	global_list.append(main(a))
	return global_list