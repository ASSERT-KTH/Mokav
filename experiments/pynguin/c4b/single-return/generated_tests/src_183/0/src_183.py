def func(*args):
	
	
	def main():
	    damage_numbers = list()
	    dragons_hurt = 0
	    damage_numbers.append(int(args[0]))
	    damage_numbers.append(int(args[1]))
	    damage_numbers.append(int(args[2]))
	    damage_numbers.append(int(args[3]))
	    num_dragons = int(args[4])
	    for dragon_num in range(num_dragons):
	        for damage_number in damage_numbers:
	            if (((dragon_num + 1) % damage_number) == 0):
	                dragons_hurt += 1
	                break
	    return(dragons_hurt)
	if (__name__ == '__main__'):
	    main()
