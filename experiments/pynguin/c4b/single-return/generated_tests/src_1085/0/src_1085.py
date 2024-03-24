def func(*args):
	
	from typing import List, Tuple
	
	def is_row_clear(board: List[str], time: int, x: int, y: int) -> bool:
	    if all(((row[y] != 'S') for row in board)):
	        return True
	    first_statue_index = [row[y] for row in board].index('S')
	    if ((first_statue_index + time) > x):
	        return True
	    else:
	        return False
	
	def moves(x: int, y: int) -> List[Tuple[(int, int)]]:
	    adj = [((x - 1), (y - 1)), ((x - 1), y), ((x - 1), (y + 1)), (x, (y - 1)), (x, (y + 1)), ((x + 1), (y - 1)), ((x + 1), y), ((x + 1), (y + 1)), (x, y)]
	    return [(xo, yo) for (xo, yo) in adj if ((0 <= xo < 8) and (0 <= yo < 8))]
	
	def solve(board: List[str]) -> str:
	    stack = [(0, idx, idy) for (idx, line) in enumerate(board) for (idy, sq) in enumerate(line) if (board[idx][idy] == 'M')]
	    while stack:
	        (time, idx, idy) = stack.pop()
	        if (is_row_clear(board, time, idx, idy) or (idx == 0)):
	            return 'WIN'
	        for (xo, yo) in moves(idx, idy):
	            if ((board[(xo - time)][yo] != 'S') and (board[((xo - 1) - time)][yo] != 'S')):
	                stack.append(((time + 1), xo, yo))
	    return 'LOSE'
	board = [args[0] for _ in range(8)]
	return(solve(board))
