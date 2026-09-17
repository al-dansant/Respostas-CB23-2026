import random

def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """
    Gera um labirinto utilizando DFS iterativo.

    A principal diferença em relação ao generate_maze original
    é que a recursão é substituída por uma "pilha".
    """
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)] # Inicializa a matriz expandida com todas as células como parede
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    pilha = [] # A pilha armazena a posição atual e o estado da busca.
    maze[1][1] = room # Inicia a busca na primeira sala.
    direcoes_iniciais = directions.copy()
    random.shuffle(direcoes_iniciais)
    pilha.append((0, 0, direcoes_iniciais, 0))

    while pilha:        
        x, y, direcoes_atuais, indice = pilha[-1] # Recupera o estado da sala que está no topo da pilha.
        # Se todas as direções já foram analisadas, realiza o retrocesso.
        if indice == len(direcoes_atuais):
            pilha.pop()
            continue

        pilha[-1] = (x, y, direcoes_atuais, indice + 1) # Atualiza o índice da próxima direção a ser analisada.
        dx, dy = direcoes_atuais[indice]
        nx = x + dx
        ny = y + dy
        
        if 0 <= nx < m and 0 <= ny < n: # Verifica se a nova sala está dentro da grade.
            if maze[2 * nx + 1][2 * ny + 1] == wall: # Verifica se a sala ainda não foi visitada.
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room # Derruba a parede entre as duas salas.
                maze[2 * nx + 1][2 * ny + 1] = room # Marca a nova sala como visitada.
                novas_direcoes = directions.copy() # Cria uma nova ordem aleatória de direções.
                random.shuffle(novas_direcoes)
                pilha.append((nx, ny, novas_direcoes, 0)) # Continua a busca a partir da nova sala.

    while True: # Posiciona o queijo em uma sala aleatória.
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break
    return maze

def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def find_cheese(maze, cheese='.'):
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == cheese: return (i, j)
    return None

def solve_maze(maze, start=(1, 1), cheese='.'):
    goal = find_cheese(maze, cheese)
    if goal is None: return None

    directions = [(-1, 0),(1, 0),(0, -1),(0, 1)]
    pilha, visitados, pais = [start], {start}, {start: None}

    while pilha:
        atual = pilha.pop()
        if atual == goal: break
        x, y = atual
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < len(maze)): continue
            if not (0 <= ny < len(maze[nx])): continue
            vizinho = (nx, ny)
            if maze[nx][ny] == 1: continue
            if vizinho in visitados: continue
            visitados.add(vizinho)
            pais[vizinho] = atual
            pilha.append(vizinho)
    if goal not in pais: return None

    caminho, atual = [], goal
    while atual is not None:
        caminho.append(atual)
        atual = pais[atual]
    caminho.reverse()
    return caminho

def print_maze_with_path(maze, path, start=(1, 1), cheese='.'):
    vermelho, branco, verde, amarelo, reset = '\033[41m', '\033[47m', '\033[42m', '\033[43m', '\033[0m'

    labirinto_visual = [row.copy() for row in maze]
    posicao_queijo = find_cheese(maze, cheese)

    if path is not None:
        for i, j in path:
            if (i, j) != start and (i, j) != posicao_queijo: labirinto_visual[i][j] = '*'
    for i, row in enumerate(labirinto_visual):
        linha = ''
        for j, elemento in enumerate(row):
            if (i, j) == start: linha += verde + '  ' + reset
            elif (i, j) == posicao_queijo: linha += amarelo + '🧀' + reset
            elif elemento == '*': linha += verde + '  ' + reset
            elif elemento == 1: linha += vermelho + '  ' + reset
            else: linha += branco + '  ' + reset
        print(linha)

if __name__ == '__main__':
    m, n = 10, 14  # Grid size
    random.seed(10110)
    maze = generate_maze(m, n)
    print('\nLabirinto gerado com DFS iterativo:\n')
    print_maze_with_path(maze, None)
    print('\nLabirinto resolvido (caminho encontrado):\n')
    path = solve_maze(maze,start=(1, 1))
    print_maze_with_path(maze,path,start=(1, 1))

    if path is not None: print(f'\nTamanho do caminho: {len(path)}')
    else: print('\nNenhum caminho encontrado.')