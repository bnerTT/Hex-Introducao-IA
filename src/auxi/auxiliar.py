def realizar_movimento(tabuleiro, linha, coluna, jogador, tamanho):
    if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
        print("Movimento inválido: Coordenadas fora do tabuleiro.")
        return False
    
    if tabuleiro[linha][coluna] != 0:
        print("Movimento inválido: Casa já ocupada.")
        return False
    
    tabuleiro[linha][coluna] = jogador
    return True

def desfazer_movimento(tabuleiro, linha, coluna, jogador,tamanho):
    if 0 <= linha < tamanho and 0 <= coluna < tamanho:
        # Se a casa não estava vazia, nós a esvaziamos
        if tabuleiro[linha][coluna] != 0:
            tabuleiro[linha][coluna] = 0
            return True
            
    return False

def verificar_vitoria(tabuleiro, grafo, jogador, tamanho):
    """
    Usa Busca em Profundidade (DFS) para checar se o jogador conectou as bordas opostas.
    """
    visitados = set()
    pilha = []
    
    # 1. Popula a pilha inicial com as peças que tocam a borda de largada
    if jogador == 1:
        # Jogador 1 tenta conectar Esquerda (coluna 0) -> Direita
        for linha in range(tamanho):
            if tabuleiro[linha][0] == 1:
                pilha.append((linha, 0))
                visitados.add((linha, 0))
    else:
        # Jogador 2 tenta conectar Cima (linha 0) -> Baixo
        for coluna in range(tamanho):
            if tabuleiro[0][coluna] == 2:
                pilha.append((0, coluna))
                visitados.add((0, coluna))
                
    # 2. Roda a Busca em Profundidade
    while pilha:
        casa_atual = pilha.pop()
        linha_atual, coluna_atual = casa_atual
        
        # 3. Verifica se a casa atual tocou a borda de chegada
        if jogador == 1 and coluna_atual == tamanho - 1:
            return True
            
        if jogador == 2 and linha_atual == tamanho - 1:
            return True
            
        # 4. Procura o próximo passo olhando os vizinhos no Grafo
        for vizinho in grafo[casa_atual]:
            vizinho_linha, vizinho_coluna = vizinho
            
            # Se o vizinho tem uma peça nossa e ainda não fomos lá, adicionamos na pilha
            if (vizinho not in visitados) and (tabuleiro[vizinho_linha][vizinho_coluna] == jogador):
                visitados.add(vizinho)
                pilha.append(vizinho)
                
    # Se a pilha acabar e não tiver tocado a borda de chegada, não venceu
    return False