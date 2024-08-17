import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import linkedList as lkl

class Cell:
    def __init__(self, line, column, value):
        self.i = line
        self.j = column
        self.value = value



# Grid size
N = 100
# Create an initial random grid
p0, p1 = 0.8, 0.2
grid = np.random.choice([0, 1], N*N, p=[p0, p1]).reshape((N, N))
ListOfAlive = lkl.LinkedList()

# ideia: pegar a grid e identificar todas as células (valores 1 no vetor bidimensional)
#        e colocá-las em uma lista linkada pra que em cada atualização do jogo não seja
#        necessário fazer um if else pra pegar todas as celular e aplicar as condições

# complementação da ideia: para não ter que checar todas as células mortas individualmente, 
#        checar apenas as que estão adjacentes às vivas.

# iterar sobre os valores da matriz para identificar as células vivas e colocar na lista linkada
for i in range(100):
    # linha "i"
    for j in range(100):
        #coluna "j"
        if grid[i, j] == 1:
            ListOfAlive.insertAtEnd(Cell(i, j, grid[i, j]))


def update(frameNum, img, grid):
    # Programar as regras de atualizacao
    plt.title(f"Game of Life - Frame {frameNum}")

        # REGRAS:
        # 1 - Qualquer célula viva com menos de dois vizinhos vivos morre; 
        # 2 - Qualquer célula viva com dois ou três vizinhos vivos continua viva para a próxima geração;
        # 3 - Qualquer célula viva com mais de três vizinhos vivos morre;
        # 4 - Qualquer célula morta com exatamente três vizinhos vivos torna-se uma célula viva.
        # após as alterações feitas no grid
    
    
    newGrid = np.zeros((100, 100), dtype=int)
    # primeiro checamos a parte interna do grid
    for i in range(1, 98):
    # linha "i"
        for j in range(1, 98):
            #coluna "j"
            sum = 0

            if grid[i, j - 1]:
                sum += 1
            
            if grid[i, j + 1]:
                sum += 1

            for num in range(3):
                if grid[(i - 1), (j - 1 + num)]:
                    sum += 1

                if grid[(i + 1), (j - 1 + num)]:
                    sum += 1

            # se a quantidade de células vivas é menor que 2 o newGrid continua com o valor igual a zero
            if grid[i, j] and (sum < 2 or sum > 3):
                newGrid[i, j] = 0

            elif grid[i, j] and (sum == 2 or sum == 3):
                newGrid[i, j] = 1

            elif grid[i, j] == 0 and sum == 3:
                newGrid[i, j] = 1
    

    for i in [0, 99]:
        for j in range(100):
            #coluna "j"
            sum = 0

            match i:
                case 0:
                    match j:
                        case 0:
                            # right
                            if grid[i, j + 1]:
                                sum += 1

                            # down
                            for num in range(2):
                                if grid[(i + 1), (j + num)]:
                                    sum += 1
                        case 99:
                            # left
                            if grid[i, j - 1]:
                                sum += 1

                            # down
                            for num in range(2):
                                if grid[(i + 1), (j  - 1 + num)]:
                                    sum += 1
                        case _:

                            # left
                            if grid[i, j - 1]:
                                sum += 1
                            
                            # right
                            if grid[i, j + 1]:
                                sum += 1
                            
                            # down
                            for num in range(3):
                                if grid[(i + 1), (j - 1 + num)]:
                                    sum += 1
                
                case 99:
                    match j:
                        case 0:
                            # right
                            if grid[i, j + 1]:
                                sum += 1

                            # up
                            for num in range(2):
                                if grid[(i - 1), (j + num)]:
                                    sum += 1
                        case 99:
                            # left
                            if grid[i, j - 1]:
                                sum += 1

                            # up
                            for num in range(2):
                                if grid[(i - 1), (j - 1 + num)]:
                                    sum += 1
                        case _:
                            # left
                            if grid[i, j - 1]:
                                sum += 1
                            
                            # right
                            if grid[i, j + 1]:
                                sum += 1
                            
                            # down
                            for num in range(3):
                                if grid[(i - 1), (j - 1 + num)]:
                                    sum += 1

            # se a quantidade de células vivas é menor que 2 o newGrid continua com o valor igual a zero
            if grid[i, j] and (sum < 2 or sum > 3):
                newGrid[i, j] = 0

            elif grid[i, j] and (sum == 2 or sum == 3):
                newGrid[i, j] = 1

            elif grid[i, j] == 0 and sum == 3:
                newGrid[i, j] = 1

    
    for i in range(1, 98):
        for j in [0, 99]:
            sum = 0
            match j:
                case 0:
                    # left
                    if grid[i - 1, j]:
                        sum += 1
                    
                    # right
                    if grid[i + 1, j]:
                        sum += 1
                    
                    # down
                    for num in range(3):
                        if grid[(i - 1 + num), (j + 1)]:
                            sum += 1
                case 99:
                    # left
                    if grid[i - 1, j]:
                        sum += 1
                    
                    # right
                    if grid[i + 1, j]:
                        sum += 1
                    
                    # down
                    for num in range(3):
                        if grid[(i - 1 + num), (j - 1)]:
                            sum += 1
            
            # se a quantidade de células vivas é menor que 2 o newGrid continua com o valor igual a zero
            if grid[i, j] and (sum < 2 or sum > 3):
                newGrid[i, j] = 0

            elif grid[i, j] and (sum == 2 or sum == 3):
                newGrid[i, j] = 1

            elif grid[i, j] == 0 and sum == 3:
                newGrid[i, j] = 1


    img.set(data=newGrid)
    return img, newGrid

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=120, interval=1000)
plt.show()