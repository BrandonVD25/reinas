import sys
sys.setrecursionlimit(15000)
import pygame

def calcularAtaques(v):
  n = len(v)
  ataques = 0
  for i in range(n-1):
    for j in range(i+1, n):
      if v[i] == v[j] or (abs(i-j)) - (abs(v[i] - v[j])) == 0:
        ataques+=2
  return ataques

def goalTest(v):
  return calcularAtaques(v) == 0


class Nodo:
    def __init__(self, estado, nivel):
        self.estado = estado
        self.nivel = nivel

def expand(edo_actual, nivel):
    n = len(edo_actual)
    queens = [" "]*n
    estadoAux = edo_actual[:]
    nivel += 1

    for i in range(0,n):
        edo_actual = estadoAux[:]

        if(edo_actual[i] > n):
            break

        edo_actual[i] = edo_actual[i] + 1
        queens[i] = Nodo(edo_actual.copy(), nivel)

    return queens


def b_profundidad_limitada(Frontera, Limite):

    if not Frontera:
        return False

    edo_actual = Frontera[0].estado
    nivel_edo_actual = Frontera[0].nivel
    Frontera.pop(0)

    drawQueens(edo_actual)

    print("EA: ",edo_actual, ",Nivel: ", nivel_edo_actual)


    if(goalTest(edo_actual)):

        print("Solucion encontrada: ", edo_actual, ", en el nivel: ", nivel_edo_actual)

        return True
    else:
        if(Limite > nivel_edo_actual):
            OffSpring = expand(edo_actual, nivel_edo_actual)
            n = len(OffSpring) - 1

            for i in range(n,-1,-1):
                if(not(OffSpring[i] == ' ')):
                    Frontera.insert(0,OffSpring[i])

    return b_profundidad_limitada(Frontera, Limite)

NQ = 4
nodo = Nodo([1]*NQ, 0)
Frontera = [nodo]
Limite=6

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

    b_profundidad_limitada(Frontera,Limite)

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
        val=EA[i]
        pygame.draw.circle(SCREEN, BLACK, [i * PIXELSIZE + 9, (val-1)* PIXELSIZE + 9], 9)

    pygame.display.update()
    #pygame.time.wait(10)

main()