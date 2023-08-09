from queue import PriorityQueue
import pygame

# Finding the width of the window

WIDTH = 800

WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")



Blue = (0,0,255)
Green = (0,255,0)
Red = (255,0,0)
White = (255,255,255)
Grey = (70,70,70)
Black = (0,0,0)
Yellow = (255,255,0)
Purple = (128,0,128)
Orange = (255,165,0)
Turquoise = (64,224,208)

class Spots:
    def __init__ (self, Row,Col,Width,TotalRows):
        self.Row = Row
        self.Col = Col
        self.x = Row * Width
        self.y = Col * Width
        self.color = White
        self.neighbors = []
        self.Width = Width
        self.TotalRows = TotalRows

    
    def GetPos(self):
        return  self.Row,self.Col

    def IsClosed(self):
         return self.color == Red
    
    def IsOpen(self):
         return self.color == Green
    
    def IsObstacle(self):
         return self.color == Black
        
    def IsStart(self):
         return self.color == Orange
    
    def IsEnd(self):
         return self.color == Turquoise
    
    def Reset(self):
         self.color == White

    def MakeClose(self):
         self.color == Red
    
    def MakeOpen(self):
         self.color == Green
    
    def MakeObstacle(self):
         self.color == Black   
     
    def MakeEnd(self):
         self.color == Turquoise
    
    def MakePath(self):
         self.color == Purple
    
    def MakeStart(self):
        self.color = Orange
    
    def Draw(self,Win):
        pygame.draw.rect(Win,self.color,(self.x,self.y,self.Width,self.Width) )
    
    def UpdateNeighbors (self, grid):
        self.neighbors = []
        if self.Row < self.TotalRows - 1 and not grid[self.Row + 1][self.Col].IsObstacle(): # DOWN
                self.neighbors.append(grid[self.Row + 1][self.Col])

        if self.Row < 0 and not grid[self.Row - 1][self.Col].IsObstacle(): # UP
            self.neighbors.append(grid[self.Row ][self.Col + 1])

        if self.Col < self.TotalRows - 1 and not grid[self.Row][self.Col + 1].IsObstacle(): # RIGHT
                self.neighbors.append(grid[self.Row - 1][self.Col])

        if self.Col < 0 and not grid[self.Row][self.Col - 1].IsObstacle(): # LEFT
                self.neighbors.append(grid[self.Row ][self.Col - 1])


    def __lt__(self, other):
        return False
    
    # Calculating the ManHatten Distance
def h(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    return abs(x1 - x2) + abs (y1 - y2)

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()


def algorithm (draw,grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}
    g_score = {spot: float("inf") for row in grid for spot in row}
    g_score[start] = 0 # Start Node
    f_score = {spot: float("inf") for row in grid for spot in row}
    f_score[start] = h(start.GetPos(), end.GetPos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.MakeEnd()
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h(neighbor.GetPos(), end.GetPos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.MakeOpen()

        draw()

        if current != start:
            current.MakeClose()
    return False


def MakeGrid (rows, width):
    Grid = []
    Gap = width // rows

    for i in range (rows):
        Grid.append([])
        for j in range (rows):
            spot = Spots(i,j,Gap,rows)
            Grid[i].append(spot)

    return Grid



def Draw_Grid (win, rows, width):
    gap = width // rows
    for i in range (rows):
        pygame.draw.line(win,Grey,(0,i*gap),(width,i*gap))
        for j in range (rows):
            pygame.draw.line(win,Grey,(j*gap,0),(j*gap,width))


# This method is to draw the lines in between and fill those grid with the colors we need
def Draw (win, grid, rows, width):
    win.fill(White)

    for row in grid:
        for spot in row:
            spot.Draw(win)
    
    Draw_Grid(win,rows,width)
    pygame.display.update()

def Get_ClickedPos (pos, rows, width):
    gap = width //rows
    y,x = pos

    row = y// gap
    col = x // gap
    return row, col


def Main(win, width):
    ROWS = 50
    grid = MakeGrid(ROWS,width)

    start = None
    end = None 
    run = True 


    while run:
        Draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
    
            if pygame.mouse.get_pressed()[0]: # Left Button
                pos = pygame.mouse.get_pos()
                row, col = Get_ClickedPos(pos,ROWS,width)
                spot = grid [row][col]
                if not start and spot!=end:
                    start = spot
                    start.MakeStart()
                    
                elif not end and spot!= start:
                   end = spot 
                   end.MakeEnd()
                
                elif spot != end and spot != start:
                    spot.MakeObstacle()

            elif pygame.mouse.get_pressed()[2]: # # Right Button mouse
                pos = pygame.mouse.get_pos()
                row, col = Get_ClickedPos(pos,ROWS,width)
                spot = grid [row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for spot in row:
                                spot.UpdateNeighbors(grid)   
                    algorithm(lambda: Draw(win, grid, ROWS, width), grid, start, end) 
                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = MakeGrid(ROWS, width)
    pygame.quit()


Main(WIN,WIDTH)













    


    # pygame.event.clear()
    # pygame.event.wait(0)

    



