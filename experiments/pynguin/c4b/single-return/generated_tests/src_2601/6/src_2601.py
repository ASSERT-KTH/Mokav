def func(*args):
	
	smith = [4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346, 355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576, 588, 627, 634, 636, 645]
	
	def main():
	    number = int(args[0])
	    return(smith[(number - 1)])
	if (__name__ == '__main__'):
	    main()
