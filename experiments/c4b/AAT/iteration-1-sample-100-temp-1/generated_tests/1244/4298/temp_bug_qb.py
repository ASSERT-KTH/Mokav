def original_func(*args):
	global_list = []
	
	from sys import setrecursionlimit
	setrecursionlimit(1000000000)
	
	def main():
	    (a, b, c) = [int(i) for i in args[0].split()]
	    if ((c % a) == 0):
	        global_list.append('-1')
	        return 0
	    p = (c // a)
	    if (p == 0):
	        if ((b > (((- 1) * a) / 2)) and (b < (a / 2))):
	            global_list.append('1')
	            return 0
	    elif ((p % 2) == 0):
	        if ((b > ((- 1) * a)) and (b < 0)):
	            global_list.append(((p // 2) * 3))
	            return 0
	        if ((b < a) and (b > 0)):
	            global_list.append((((p // 2) * 3) + 1))
	            return 0
	    elif ((b > (((- 1) * a) // 2)) and (b < (a // 2))):
	        global_list.append((((p // 2) * 3) + 2))
	        return 0
	    global_list.append('-1')
	main()
	return global_list