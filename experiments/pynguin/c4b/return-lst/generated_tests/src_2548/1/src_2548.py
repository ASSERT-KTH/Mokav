def func(*args):
	ret_values = []
	
	import sys
	
	def left_tile(tile):
	    return ((tile[0] - 1), tile[1])
	
	def right_tile(tile):
	    return ((tile[0] + 1), tile[1])
	
	def upper_tile(tile):
	    return (tile[0], (tile[1] + 1))
	
	def lower_tile(tile):
	    return (tile[0], (tile[1] - 1))
	
	def nearby_tiles(tile, move):
	    if (move == 'L'):
	        return {upper_tile(tile), lower_tile(tile), right_tile(tile)}
	    elif (move == 'R'):
	        return {upper_tile(tile), lower_tile(tile), left_tile(tile)}
	    elif (move == 'U'):
	        return {left_tile(tile), lower_tile(tile), right_tile(tile)}
	    else:
	        return {left_tile(tile), upper_tile(tile), right_tile(tile)}
	
	def is_shortest_path(robot_path, change_position):
	    reached_tiles = set()
	    position = (0, 0)
	    reached_tiles.update([position])
	    for move in robot_path:
	        reached_tiles.update(nearby_tiles(position, move))
	        position = change_position[move](position)
	        if (position in reached_tiles):
	            return False
	        reached_tiles.update([position])
	    return True
	
	def main(sinp=sys.stdin, sout=sys.stdout):
	    robot_path = sinp.readline().strip()
	    change_position = {'L': left_tile, 'R': right_tile, 'U': upper_tile, 'D': lower_tile}
	    result = ('OK' if is_shortest_path(robot_path, change_position) else 'BUG')
	    sout.write(result)
	if (__name__ == '__main__'):
	    main()

	return ret_values
