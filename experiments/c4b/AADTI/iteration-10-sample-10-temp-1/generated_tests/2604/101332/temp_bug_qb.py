def original_func(*args):
	global_list = []
	
	
	def sol(number):
	    num = list(map(int, str(number)))
	    mmm = sum(num)
	    length = len(num)
	    for i in reversed(range((length - 1))):
	        if num[i]:
	            num[i] -= 1
	            for j in range((i + 1), length):
	                num[j] = 9
	            if (mmm < sum(num)):
	                number = int(''.join(map(str, num)))
	    return number
	global_list.append(sol(int(args[0])))
	return global_list