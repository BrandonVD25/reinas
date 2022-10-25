import sys
sys.setrecursionlimit(15000)
import pygame

def CalcularAtaques(v):
  n = len(v)
  ataques = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if v[i] == v[j] or (abs(i-j)) - (abs(v[i] - v[j])) == 0:
        ataques+=2
  return ataques

def goalTest(v):
  return CalcularAtaques(v) == 0

class Nodo:
    def __init__(self, estado, ataques):
        self.estado = estado
        self.ataques = ataques

def expand(EdoActual):
    Nlength = len(EdoActual) 
    queens = []
    estadoAux = EdoActual[:]

    for i in range(0,Nlength):
        EdoActual = estadoAux[:]
        for j in range(0,Nlength-1): 
            if(EdoActual[i] < Nlength-1):
                EdoActual[i] = EdoActual[i] + 1
            else:
                EdoActual[i] = j

            if(EdoActual != estadoAux):
                queens.append(Nodo(EdoActual.copy(), None))

    return queens

def evaluateAttacks(Offspring):
    for i in range(len(Offspring)):
        numberAttacks = CalcularAtaques(Offspring[i].estado)
        Offspring[i].ataques = numberAttacks

def B_Voraz(Front):
    if not Front:
        return None
    
    EA = Front.pop(0)
    print("EA: ", EA)
    print("Ataques: ", CalcularAtaques(EA))
    drawQueens(EA)

    if(goalTest(EA)):
        print("Solucion encontrada")
        return EA
    
    OffSpring = expand(EA)
    evaluateAttacks(OffSpring)
    OffSpring.sort(key=lambda x:x.ataques)

    while(True):
        firstNode = OffSpring.pop(0)
        if firstNode.estado in visitedList:
            continue
        else:
            visitedList.append(firstNode.estado)    
            Front.append(firstNode.estado)
            break
    
    return B_Voraz(Front)
#Front  
visitedList = []
NQ = 50
Frontera = [[0]*NQ]


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHESS1 = (181, 136, 99)
CHESS2 = (240, 217, 181)


PIXELSIZE = 18

WINDOW_HEIGHT = PIXELSIZE * NQ
WINDOW_WIDTH = PIXELSIZE * NQ

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    B_Voraz(Frontera)

    pygame.time.wait(500000)

def drawBoard():

    for i in range(NQ):
        for j in range(NQ):
            color = CHESS1
            if((i+j) %2 == 0):
                color = CHESS2
            pygame.draw.rect(SCREEN, color,[i * PIXELSIZE, j * PIXELSIZE,PIXELSIZE,PIXELSIZE])
    pygame.display.update()

def drawQueens(EA):
    drawBoard()
    for i in range(len(EA)):  
        pygame.draw.circle(SCREEN, BLACK, [i * PIXELSIZE + 9, EA[i]* PIXELSIZE + 9], 9)

    pygame.display.update()
    #pygame.time.wait(10)

main()
