def func(*args):
	
	
	def main():
	    (a, b, c, d, e) = (int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]))
	    harm = [a, b, c, d]
	    nums = set(range(1, (e + 1)))
	    nums2 = set(range(1, (e + 1)))
	    for x in range(0, 4):
	        for y in nums2:
	            if ((y % harm[x]) == 0):
	                if (y in nums):
	                    nums.remove(y)
	    return((e - len(nums)))
	if (__name__ == '__main__'):
	    main()
