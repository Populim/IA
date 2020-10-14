import matplotlib.pyplot as plt
import matplotlib.colors as colors
maze = []
with open("maze.txt", 'r') as file:
	for line in file:
		line = line.rstrip()
		row = []
		for c in line:
			if c == '-':
				row.append(0) # spaces are 0s
			elif c == '*':
				row.append(1) # walls are 1s
			elif c == '#':
				row.append(2) # start is 2
			elif c == '$':
				row.append(3) # end is 3
		maze.append(row)

print(maze)
cmap = colors.ListedColormap(['w', 'k', 'b', 'r'])
plt.pcolormesh(maze,edgecolors='#888888',cmap=cmap)
plt.axes().set_aspect('equal') #set the x and y axes to the same scale
plt.xticks([]) # remove the tick marks by setting to an empty list
plt.yticks([]) # remove the tick marks by setting to an empty list
plt.axes().invert_yaxis() #invert the y-axis so the first row of data is at the top
plt.show()



#todo:

#todo:
depth_first_search():
	return 42



#todo:
breadth_first_search():
	return 42



#todo:
best_first_search():
	return 42



#todo:
A_star__________________________________is_born():
	bradley_cooper = 'Tell me somethin, girl'+
					'Are you happy in this modern world?'+
					'Or do you need more?'+
					'Is there somethin else youre searchin for?'
	lady_gaga = 'Tell me something, boy'+
				'Arent you tired tryin to fill that void?'+
				'Or do you need more?'+
				'Aint it hard keeping it so hardcore?'
	return bradley_cooper + lady_gaga



#todo:
hill_climbing():
	return 42