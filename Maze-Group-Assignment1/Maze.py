import copy

class Queue:
    L = []
    def __init__(self):
        print(self.L)
    def enqueue(self,element):
        self.L.append(element)
    def dequeue(self):
        if(self.isEmpty() == False):
            return self.L.pop(0)
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class Stack:
    L = []
    def __init__(self):
        print(self.L)
    def push(self,element):
        self.L.append(element)
    def pop(self):
        if(self.isEmpty() == False):
            return self.L.pop()
        else:
            return None
    def count(self):
        return len(self.L)
    def isEmpty(self):
        return self.count() == 0
################
class MazeNode:
    def __init__(self, x, y, isLeft, isRight, isTop, isBottom):
        self._x = x
        self._y = y
        self._isLeft = isLeft
        self._isRight = isRight
        self._isTop = isTop
        self._isBottom = isBottom
################
class Maze:
    def __init__(self, xSquare, ySquare):
        self._xSquare = xSquare
        self._ySquare = ySquare
        self._maze = []
        self._startNode = None
        self._goalNode = None
        self.initializeMaze()

    def initializeMaze(self):
        for i in range(self._ySquare):
            row = []
            for j in range(self._xSquare):
                row.append(None)
            self._maze.append(row)

    def setStartNode(self, x, y):
        self._startNode = (x, y)

    def setGoalNode(self, x, y):
        self._goalNode = (x, y)

    def addMazeSquare(self, x, y, isLeft, isRight, isTop, isBottom):
        newMazeSquare = MazeNode(x, y, isLeft, isRight, isTop, isBottom)
        self._maze[y][x] = newMazeSquare

    def getMazeNodeByXY(self, x, y):
        return self._maze[y][x]

    def getMazeNodeByCoords(self, coords):
        return self._maze[coords[1]][coords[0]]

    def getMazeNodeChildren(self, x, y):
        children = []
        if (x > 0 and not self._maze[y][x]._isLeft):
            children.append((self._maze[y][x - 1]._x, self._maze[y][x - 1]._y))
        if (x < self._xSquare - 1 and not self._maze[y][x]._isRight):
            children.append((self._maze[y][x + 1]._x, self._maze[y][x + 1]._y))
        if (y > 0 and not self._maze[y][x]._isTop):
            children.append((self._maze[y - 1][x]._x, self._maze[y - 1][x]._y))
        if (x < self._ySquare - 1 and not self._maze[y][x]._isBottom):
            children.append((self._maze[y + 1][x]._x, self._maze[y + 1][x]._y))
        return children

    def depthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        stack = Stack()
        stack.push([self._startNode])
        paths = []

        while (not stack.isEmpty()):
            currentPath = stack.pop()
            currentXY = currentPath[-1]
            if (self._goalNode == currentXY):
                paths.append(currentPath)
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            for child in currentChildren:
                if (child in currentPath):
                    continue
                stack.push(currentPath + [child])
        return paths

    def breadthFirstTraverse(self):
        if (self._startNode is None or self._goalNode is None):
            return None

        queue = Queue()
        queue.enqueue([self._startNode])
        paths = []

        while (not queue.isEmpty()):
            currentPath = queue.dequeue()
            currentXY = currentPath[-1]
            if (self._goalNode == currentXY):
                paths.append(currentPath)
            currentNode = self.getMazeNodeByCoords(currentXY)
            currentChildren = self.getMazeNodeChildren(currentXY[0], currentXY[1])[::-1]
            for child in currentChildren:
                if (child in currentPath):
                    continue
                queue.enqueue(currentPath + [child])
        return paths



##########################
# Main App

game = Maze(7, 6)


# (x, y, isLeft, isRight, isTop, isBottom)
# First Row
game.addMazeSquare(0, 0, True, False, True, False)
game.addMazeSquare(1, 0, False, False, True, True)
game.addMazeSquare(2, 0, False, False, True, False)
game.addMazeSquare(3, 0, False, True, True, False)
game.addMazeSquare(4, 0, True, False, True, False)
game.addMazeSquare(5, 0, False, False, True, False)
game.addMazeSquare(6, 0, False, True, True, True)



