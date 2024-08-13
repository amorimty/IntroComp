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
    
    # if (ListOfAlive.head):
    #     currentNode = ListOfAlive.head

    #     while (currentNode):
    #         sum = 0

    #         for num in range(3):
    #             if ((currentNode.data.i - 1) >= 0) and grid[(currentNode.data.i - 1), (currentNode.data.j - 1 + num)]):



    #         up, down, left, right = 0
    #         if (currentNode.data.i - 1) >= 0 and currentNode.data.value[(currentNode.data.i - 1), currentNode.data.j]:
    #             up = 1

    #         if (currentNode.data.i + 1) <= 99 and currentNode.data.value[(currentNode.data.i + 1), currentNode.data.j]:
    #             down = 1
            
    #         if (currentNode.data.j - 1) >= 0 and currentNode.data.value[currentNode.data.i, (currentNode.data.j - 1)]:
    #             left = 1
            

    #         if (currentNode.data.j + 1) >= 0 and currentNode.data.value[currentNode.data.i, (currentNode.data.j + 1)]:
    #             right = 1
            
    #         match sum:
    #             case (sum < 2):
                    
    #             case
            
    for i in range(100):
    # linha "i"
        for j in range(100):
            #coluna "j"
            for num in range(3):
                if (i > 0 and i < 99):
                    

    return img

fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid), frames=120, interval=30)
plt.show()