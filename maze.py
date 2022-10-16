import time
import os
"""
maze = [
		['$', '$', '$', '$', '$'],
		['$', ' ', ' ', 'o', '$'],
		['$', ' ', ' ', ' ', '$'],
		['$', 'x', ' ', ' ', '$'],
		['$', '$', '$', '$', '$']
		]
"""

"""
maze = [

    ["$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$"],
    ["$", " ", " ", " ", " ", " ", " ", "o", "$", " ", "$"],
    ["$", " ", " ", "$", "$", "$", "$", "$", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", "x", "$", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$"]

    ]
"""
maze = [

    ["$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", "x", "$"],
    ["$", "$", " ", "$", "$", "$", "$", "$", "$", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", "$", " ", "$"],
    ["$", " ", "$", "$", "$", "$", "$", " ", "$", " ", "$"],
    ["$", " ", "$", " ", " ", "o", "$", " ", "$", " ", "$"],
    ["$", " ", "$", " ", "$", "$", "$", " ", "$", " ", "$"],
    ["$", " ", "$", " ", " ", " ", " ", " ", "$", " ", "$"],
    ["$", " ", "$", "$", "$", "$", "$", "$", "$", " ", "$"],
    ["$", " ", " ", " ", " ", " ", " ", " ", " ", " ", "$"],
    ["$", "$", "$", "$", "$", "$", "$", "$", "$", "$", "$"]

    ]
    

def startingPos(maze):
    for i in range(len(maze)):
        if 'o' not in maze[i]: continue

        return i, maze[i].index('o')

def endingPos(maze):
    for i in range(len(maze)):
        if 'x' not in maze[i]: continue

        return i, maze[i].index('x')

def adjacentNodes(x, y):
	l = []

	if maze[x - 1][y] != '$':
		l.append([x - 1, y])

	if maze[x + 1][y] != '$':
		l.append([x + 1, y])

	if maze[x][y - 1] != '$':
		l.append([x, y - 1])

	if maze[x][y + 1] != '$':
		l.append([x, y + 1])

	return l


def bfs(x1, y1, x2, y2, maze):
	prev = solve(x1, y1, maze)
	return reconstruct(x1, y1, x2, y2, prev), prev

def solve(x1, y1, maze):
	l = [[x1, y1]]

	m = [x[:] for x in maze]

	m[x1][y1] = True
	prev = {}

	while l != []:
		x = l[0][0]
		y = l[0][1]

		l.pop(0)
		neighbours = adjacentNodes(x, y)

		for x1, y1 in neighbours:
			if m[x1][y1] == 'x':
				prev[x1, y1] = [x, y]
				return prev
			elif m[x1][y1] == ' ':
				l.append([x1, y1])
				m[x1][y1] = True
				prev[x1, y1] = [x, y]

	return prev

def reconstruct(x1, y1, x2, y2, prev):
	path = []

	currX = x2
	currY = y2


	while (currX, currY) in prev:
		path.append([currX, currY])

		t = prev[currX, currY]

		currX = t[0]
		currY = t[1]

	path.append([currX, currY])

	path.reverse()

	if path[0] == [x1, y1]:
		return path
	return []



def alterMaze(m):
	x = 0

	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] != '$':
				m[i][j] = [x, False]
				x += 1
	return m


def printAns(l, prev):
	for i in prev:
		printMaze()
		time.sleep(0.1)
		if l == []:
			return
		os.system('cls')
		
		x = l[0][0]
		y = l[0][1]

		maze[x][y] = '+'

		
		l.pop(0)

def printMaze():
	for row in maze:
		print("".join(row))
		
	
x1, y1 = startingPos(maze)
x2, y2 = endingPos(maze)
l, prev = bfs(x1, y1, x2, y2, maze)

printAns(l, prev)


