def gerar_grafo_hex(tamanho):
    """
    Gera o dicionário de vizinhança para um tabuleiro Hex de tamanho N x N.
    """
    grafo = {}
    
    # As 6 direções adjacentes em um sistema de coordenadas Hexaxial
    direcoes = [
        (-1, 0),  # Cima-Esquerda
        (-1, 1),  # Cima-Direita
        (0, -1),  # Esquerda
        (0, 1),   # Direita
        (1, -1),  # Baixo-Esquerda
        (1, 0)    # Baixo-Direita
    ]
    
    for linha in range(tamanho):
        for coluna in range(tamanho):
            casa_atual = (linha, coluna)
            vizinhos_validos = []
            
            # Testa as 6 direções a partir da casa atual
            for delta_linha, delta_coluna in direcoes:
                nova_linha = linha + delta_linha
                nova_coluna = coluna + delta_coluna
                
                # Garante que o vizinho não está fora dos limites do tabuleiro
                if 0 <= nova_linha < tamanho and 0 <= nova_coluna < tamanho:
                    vizinhos_validos.append((nova_linha, nova_coluna))
            
            grafo[casa_atual] = vizinhos_validos
            
    return grafo

def printar_grafo_organizado(grafo):
    linha_atual = -1
    
    for casa, vizinhos in grafo.items():
        linha_da_casa = casa[0]
        
        # Cria um cabeçalho visual sempre que pular para uma nova linha no tabuleiro
        if linha_da_casa != linha_atual:
            print(f"\n[{'-'*10} Linha {linha_da_casa} {'-'*10}]")
            linha_atual = linha_da_casa
            
        # Formata a lista de vizinhos tirando os colchetes chatos
        vizinhos_str = ", ".join([str(v) for v in vizinhos])
        
        # O rjust alinha o texto à direita para que (0, 0) ocupe o mesmo espaço que (10, 10)
        casa_str = str(casa).rjust(8) 
        
        print(f"{casa_str} -> {vizinhos_str}")

# Testando com um tabuleiro menor (3x3) para ver o resultado limpo
tamanho = 3
meu_grafo = gerar_grafo_hex(tamanho)
printar_grafo_organizado(meu_grafo)

# Exemplo de uso para criar um tabuleiro 11x11
tamanho_tabuleiro = 11
meu_grafo = gerar_grafo_hex(tamanho_tabuleiro)
printar_grafo_organizado(meu_grafo)
    