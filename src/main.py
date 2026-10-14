def gerar_grafo_hex(tamanho):
    grafo = {}
    direcoes = [(-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0)]
    for linha in range(tamanho):
        for coluna in range(tamanho):
            casa_atual = (linha, coluna)
            vizinhos_validos = []
            for d_linha, d_coluna in direcoes:
                n_linha, n_coluna = linha + d_linha, coluna + d_coluna
                if 0 <= n_linha < tamanho and 0 <= n_coluna < tamanho:
                    vizinhos_validos.append((n_linha, n_coluna))
            grafo[casa_atual] = vizinhos_validos
    return grafo

def realizar_movimento(tabuleiro, linha, coluna, jogador, tamanho):
    if not (0 <= linha < tamanho and 0 <= coluna < tamanho):
        print("❌ Movimento inválido: Coordenadas fora do tabuleiro.")
        return False
    if tabuleiro[linha][coluna] != 0:
        print("❌ Movimento inválido: Casa já ocupada.")
        return False
    tabuleiro[linha][coluna] = jogador
    return True

def verificar_vitoria(tabuleiro, grafo, jogador, tamanho):
    visitados = set()
    pilha = []
    
    if jogador == 1: # Azul (Esquerda -> Direita)
        for linha in range(tamanho):
            if tabuleiro[linha][0] == 1:
                pilha.append((linha, 0))
                visitados.add((linha, 0))
    else: # Vermelho (Cima -> Baixo)
        for coluna in range(tamanho):
            if tabuleiro[0][coluna] == 2:
                pilha.append((0, coluna))
                visitados.add((0, coluna))
                
    while pilha:
        casa_atual = pilha.pop()
        linha_atual, coluna_atual = casa_atual
        
        if jogador == 1 and coluna_atual == tamanho - 1: return True
        if jogador == 2 and linha_atual == tamanho - 1: return True
            
        for vizinho in grafo[casa_atual]:
            v_linha, v_coluna = vizinho
            if (vizinho not in visitados) and (tabuleiro[v_linha][v_coluna] == jogador):
                visitados.add(vizinho)
                pilha.append(vizinho)
    return False

def imprimir_tabuleiro(tabuleiro, tamanho):
    simbolos = {0: ".", 1: "A", 2: "V"}
    print("\n" + "="*30)
    for i in range(tamanho):
        # A mágica visual do Hex: cada linha ganha um espaço extra de recuo
        espacos = " " * i 
        linha_formatada = " ".join([simbolos[peca] for peca in tabuleiro[i]])
        # Adiciona o número da linha para facilitar na hora de jogar
        print(f"{i} | {espacos}{linha_formatada}")
    print("="*30 + "\n")

def menu_jogo():
    print("=== BEM-VINDO AO JOGO HEX ===")
    print("Jogador 1 (A - Azul) tenta conectar a Esquerda com a Direita.")
    print("Jogador 2 (V - Vermelho) tenta conectar Cima com Baixo.\n")
    
    try:
        tamanho = int(input("Digite o tamanho do tabuleiro (recomendado: 5 para teste): "))
    except ValueError:
        tamanho = 5
        print("Entrada inválida. Usando tabuleiro 5x5 por padrão.")

    # Inicializa o ambiente
    tabuleiro = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    grafo = gerar_grafo_hex(tamanho)
    
    jogador_atual = 1
    jogo_rolando = True
    
    while jogo_rolando:
        imprimir_tabuleiro(tabuleiro, tamanho)
        
        nome_cor = "Azul (A)" if jogador_atual == 1 else "Vermelho (V)"
        print(f"👉 Turno do Jogador {jogador_atual} [{nome_cor}]")
        
        try:
            linha = int(input(f"Escolha a linha (0 a {tamanho-1}): "))
            coluna = int(input(f"Escolha a coluna (0 a {tamanho-1}): "))
        except ValueError:
            print("❌ Por favor, digite apenas números inteiros.")
            continue
            
        # Tenta aplicar a jogada
        if realizar_movimento(tabuleiro, linha, coluna, jogador_atual, tamanho):
            # Se a jogada foi válida, checa se ele ganhou
            if verificar_vitoria(tabuleiro, grafo, jogador_atual, tamanho):
                imprimir_tabuleiro(tabuleiro, tamanho)
                print(f"🏆 PARABÉNS! O Jogador {jogador_atual} [{nome_cor}] CONECTOU OS LADOS E VENCEU! 🏆")
                jogo_rolando = False
            else:
                # Troca o jogador (1 vira 2, 2 vira 1)
                jogador_atual = 3 - jogador_atual

# Executa o jogo
if __name__ == "__main__":
    menu_jogo()