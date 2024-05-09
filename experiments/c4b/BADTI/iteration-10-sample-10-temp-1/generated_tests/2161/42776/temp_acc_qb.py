def patched_func(*args):
	global_list = []
	
	
	def check_win(x):
	    if (x == 3):
	        return True
	    else:
	        return False
	
	def amount_x(x):
	    return x.count('X')
	
	def amount_0(x):
	    return x.count('0')
	h_line1 = list(args[0])
	h_line2 = list(args[1])
	h_line3 = list(args[2])
	board = ((h_line1 + h_line2) + h_line3)
	diagonal1 = [h_line1[0], h_line2[1], h_line3[2]]
	diagonal2 = [h_line1[2], h_line2[1], h_line3[0]]
	v_line1 = [h_line1[0], h_line2[0], h_line3[0]]
	v_line2 = [h_line1[1], h_line2[1], h_line3[1]]
	v_line3 = [h_line1[2], h_line2[2], h_line3[2]]
	if ((amount_x(board) - amount_0(board)) == 1):
	    if (check_win(amount_x(h_line1)) or check_win(amount_x(h_line2)) or check_win(amount_x(h_line3)) or check_win(amount_x(v_line1)) or check_win(amount_x(v_line2)) or check_win(amount_x(v_line3)) or check_win(amount_x(diagonal1)) or check_win(amount_x(diagonal2))):
	        conclusion = 'the first player won'
	    elif (check_win(amount_0(h_line1)) or check_win(amount_0(h_line2)) or check_win(amount_0(h_line3)) or check_win(amount_0(v_line1)) or check_win(amount_0(v_line2)) or check_win(amount_0(v_line3)) or check_win(amount_0(diagonal1)) or check_win(amount_0(diagonal2))):
	        conclusion = 'illegal'
	    elif (board.count('.') == 0):
	        conclusion = 'draw'
	    else:
	        conclusion = 'second'
	elif (amount_x(board) == amount_0(board)):
	    if (check_win(amount_0(h_line1)) or check_win(amount_0(h_line2)) or check_win(amount_0(h_line3)) or check_win(amount_0(v_line1)) or check_win(amount_0(v_line2)) or check_win(amount_0(v_line3)) or check_win(amount_0(diagonal1)) or check_win(amount_0(diagonal2))):
	        conclusion = 'the second player won'
	        if (check_win(amount_x(h_line1)) or check_win(amount_x(h_line2)) or check_win(amount_x(h_line3)) or check_win(amount_x(v_line1)) or check_win(amount_x(v_line2)) or check_win(amount_x(v_line3)) or check_win(amount_x(diagonal1)) or check_win(amount_x(diagonal2))):
	            conclusion = 'illegal'
	    elif (check_win(amount_x(h_line1)) or check_win(amount_x(h_line2)) or check_win(amount_x(h_line3)) or check_win(amount_x(v_line1)) or check_win(amount_x(v_line2)) or check_win(amount_x(v_line3)) or check_win(amount_x(diagonal1)) or check_win(amount_x(diagonal2))):
	        conclusion = 'illegal'
	    else:
	        conclusion = 'first'
	else:
	    conclusion = 'illegal'
	global_list.append(conclusion)
	return global_list