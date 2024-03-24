def func(*args):
	
	
	def winners_list(s):
	    i = ((s // 50) % 475)
	    for _ in range(25):
	        i = (((i * 96) + 42) % 475)
	        (yield (26 + i))
	
	def count_hacks():
	    (p, x, y) = args[0].split(' ')
	    p = int(p)
	    x = int(x)
	    y = int(y)
	    current_winners = list(winners_list(x))
	    if ((x >= y) and (p in current_winners)):
	        return 0
	    mix = x
	    for _ in range((x // 50)):
	        mix -= 50
	        current_winners_minus_50 = list(winners_list(mix))
	        if ((mix >= y) and (p in current_winners_minus_50)):
	            return 0
	    succesful_hacks = 0
	    won = False
	    while (not won):
	        succesful_hacks += 1
	        x += 100
	        current_winners = list(winners_list(x))
	        if ((x >= y) and (p in current_winners)):
	            return succesful_hacks
	        current_winners_minus_50 = list(winners_list((x - 50)))
	        if (((x - 50) >= y) and (p in current_winners_minus_50)):
	            return succesful_hacks
	if (__name__ == '__main__'):
	    return(count_hacks())
