def func(*args):
	ret_values = []
	
	import sys
	if False:
	    input = open('game.txt', 'r')
	else:
	    input = sys.stdin
	nums = input.readline().split()
	a = int(nums[0])
	b = int(nums[1])
	n = int(nums[2])
	win = False
	numPlayers = 2
	turn = 0
	players = []
	players.append(a)
	players.append(b)
	
	def HCF(c, d):
	    while (d > 0):
	        t = d
	        d = (c % d)
	        c = t
	    return c
	while (win != True):
	    if (n >= HCF(players[turn], n)):
	        n = (n - HCF(players[turn], n))
	        turn = ((turn + 1) % numPlayers)
	    else:
	        win = True
	ret_values.append(((turn + 1) % numPlayers))

	return ret_values
