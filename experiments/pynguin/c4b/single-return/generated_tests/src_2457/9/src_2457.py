def func(*args):
	
	
	def mod(dragon):
	    for d in damage:
	        if ((dragon % d) == 0):
	            return True
	damage = []
	damage.append(int(args[0]))
	damage.append(int(args[1]))
	damage.append(int(args[2]))
	damage.append(int(args[3]))
	d = int(args[4])
	dragons = list(range(1, (d + 1)))
	count_otpizzen = 0
	for dragon in dragons:
	    if mod(dragon):
	        count_otpizzen += 1
	return(count_otpizzen)
