import sys
sys.setrecursionlimit(30000)
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

def expand(edo_actual):
  n = len(edo_actual)
  nodos_hijos = []
  for i in range(n):
    lista_aux = list(edo_actual)
    valor_posicion = edo_actual[i]
    if valor_posicion < n:
      valor_posicion += 1
      lista_aux[i] = valor_posicion
      nodos_hijos.append(lista_aux)
    else:
      return []
  return nodos_hijos


def b_profundidad(Frontier):
    if (len(Frontier) == 0):
        return None

    edo_actual = Frontier.pop(0)
    print("EA: ",edo_actual)
    print("Ataques: ", calcularAtaques(edo_actual))
    drawQueens(edo_actual)

    if goalTest(edo_actual):
        print("Solucion encontrada")
        return edo_actual

    offSpring = expand(edo_actual)

    for element in offSpring:
        Frontier.insert(0, element)

    return b_profundidad(Frontier)


NQ = 4
Frontera = [[1]*NQ]


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CHESS1 = (181, 136, 99)
CHESS2 = (240, 217, 181)


PIXELSIZE = 18

WINDOW_HEIGHT = PIXELSIZE * (NQ)
WINDOW_WIDTH = PIXELSIZE * (NQ)

def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)


    b_profundidad(Frontera)

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
