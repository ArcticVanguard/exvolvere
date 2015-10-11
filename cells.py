class cell:
    def __init__(self, y, x, icon, cellnum, isplayable=False):
        self.chricon = icon
        self.playable = isplayable
        self.coords = [y, x]
        self.isalive = True
        self.evopoints = 0
        self.idnum = cellnum

        #TODO: Ability flags

        #TODO: Stats

        def isPlayable(self):
            return self.playable

        def getIcon(self):
            return self.chricon

        #Returns a list of form [y, x, icon], also referred to as a cell type
        def getFormattedList(self):
            return [self.coords[0], self.coords[1], self.chricon]

        #Movement functions
        def move(self, direction, board):
            if direction == 0:
                self.moveNorth(board)
            if direction == 1:
                self.moveSouth(board)
            if direction == 2:
                self.moveEast(board)
            if direction == 3:
                self.moveWest(board)

        def moveNorth(board):
            dest = [self.coords[0] - 1, self.coords[1]]
            tile = board.getTile(dest)
            passable = tile.isPassable()
            if passable:
                self.coords = dest
        def moveSouth(board):
            dest = [self.coords[0] + 1, self.coords[1]]
            tile = board.getTile(dest)
            passable = tile.isPassable()
            if passable:
                self.coords = dest
        def moveEast(board):
            dest = [self.coords[0], self.coords[1] - 1]
            tile = board.getTile(dest)
            passable = tile.isPassable()
            if passable:
                self.coords = dest
        def moveWest(board):
            dest = [self.coords[0], self.coords[1] + 1]
            tile = board.getTile(dest)
            passable = tile.isPassable()
            if passable:
                self.coords = dest
 