
import random as rnd





class Cell:
    def __init__(self,x,y):
        self.neighbours = []
        self.xPos = x
        self.yPos = y
        self.occupant = None
        self.number_neighbours =-1

    def addNeighbour(self,cell):
        self.neighbours.append(cell)
        self.number_neighbours+=1

class Agent:
    def __init__(self,state,home):
        self.home = home
        self.state = state
        self.happy = False

    def countSimilar(self):
        sim = -1 # so it does not count self
        dif =0
        for n in self.home.neighbours:
            if (n.occupant!=None):
                if (n.occupant.state == self.state):
                    sim +=1
                else:
                    dif +=1
        return sim, dif

    def getHappy(self,similar):
        sim,dif = self.countSimilar()
        self.happy = sim>=(similar*(sim+dif))

class Experiment:
    def __init__(self,size):        
        self.cells = []
        self.agents = []
        self.size = size
        self.total_cells = size*size -1
        self.total_agents = -1
        
    
    def setUp(self,numb_agents,similar):
        self.cells = []
        self.similar = similar
        for i in range(self.size*self.size):
            self.cells.append(Cell(int(i/self.size),(i%self.size)))
        for cell in self.cells:
            for  y in range(cell.yPos-1,cell.yPos+2):
                for  x in range(cell.xPos-1,cell.xPos+2):
                    x=self.bounds(x)
                    y=self.bounds(y)
                    pos = x*self.size+y
                    cell.addNeighbour(self.cells[pos])
        for _ in range(numb_agents):
            cell = self.getEmpty()
            agent = Agent(rnd.randint(1,2),cell)
            self.total_agents+=1
            self.agents.append(agent)
            cell.occupant = agent
            agent.home = cell
        
       
    def bounds(self,i):
        if i<0:
            return self.size + i 
        if i>=self.size:
            return i-self.size
        return i
        

    def getEmpty(self):
        flag = False
        while not flag:
            cell = rnd.choice(self.cells)
            flag = cell.occupant == None
        return cell

    def getMatrix(self):
        matrix = [[0 for _ in range(self.size)  ] for _ in range(self.size)]
        for cell in self.cells:
            x = cell.xPos
            y = cell.yPos
            if cell.occupant != None:
                print(cell.occupant.state)
                matrix[x][y]=cell.occupant.state
        return matrix

    def getResultMatrix(self):
        matrix = [[0 for _ in range(self.size)  ] for _ in range(self.size)]
        total =0
        happy = 0
        unhappy = 0
        similar = 0
        different =0
        for cell in self.cells:
            x = cell.xPos
            y = cell.yPos
            if cell.occupant != None:
                s, d = cell.occupant.countSimilar()
                similar += s
                different += d 
                cell.occupant.getHappy(self.similar)
                if cell.occupant.happy:
                    matrix[x][y]=cell.occupant.state
                    happy+=1
                else:
                    matrix[x][y]=cell.occupant.state
                    unhappy+=1
        total = similar+different
        return matrix,happy,unhappy

    def iterate(self):
        rnd.shuffle(self.agents)
        rnd.shuffle(self.cells)
        for agent in self.agents:
            if agent.happy==False:
                for cell in self.cells:
                    if cell.occupant==None:
                        agent.home.occupant = None;
                        agent.home = cell
                        cell.occupant = agent


   

