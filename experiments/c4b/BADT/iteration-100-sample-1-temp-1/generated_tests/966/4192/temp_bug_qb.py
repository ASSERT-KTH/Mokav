def original_func(*args):
	global_list = []
	
	(n, m, k) = [int(i) for i in args[0].split()]
	
	def one_sided(slots, x):
	    if (slots >= (x - 1)):
	        return (((slots - x) + 1) + (((x - 1) * x) // 2))
	    else:
	        return ((slots * (((2 * x) - slots) - 1)) // 2)
	
	def pillows_used(x):
	    left_slot = (k - 1)
	    right_slot = (n - k)
	    return (((x + one_sided(left_slot, x)) + one_sided(right_slot, x)) <= m)
	
	def main():
	    left = 1
	    right = m
	    mid = ((left + right) // 2)
	    if (left == right):
	        return mid
	    while (left != right):
	        if pillows_used(mid):
	            left = (mid + 1)
	        else:
	            right = mid
	        mid = ((left + right) // 2)
	    return (mid - 1)
	global_list.append(main())
	return global_list