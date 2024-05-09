def original_func(*args):
	global_list = []
	
	
	def main():
	    a = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	    (n, k) = map(int, args[0].split())
	    global_list.append(((1 + a[(n - 1)]) - (((8 - k) + 6) // 7)))
	    return 0
	main()
	return global_list