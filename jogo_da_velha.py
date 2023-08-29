import random

def definirSimbolo(modo):
    if modo == "PvP":
        sim1 = input("Jogador 1 será X ou O? ").upper()
        while sim1 != "X" and sim1 != "O":
            sim1 = input("Escolha um símbolo válido (X ou O).")
        if sim1 == "X":
            sim2 = "O"
            print("Jogador 2 será O")
        else:
            sim2 = "X"
            print("Jogador 2 será X")
    else:
        sim1 = input("Você jogará como X ou O? ").upper()
        while sim1 !=  "X" and sim1 != "O":
            sim1 = input("Escolha um símbolo válido (X ou O). ").upper()
        if sim1 == "X":
            sim2 = "O"
            print("O Computador (jogador 2) jogará como O")
        else:
            sim2 = "X"
            print("O Computador (jogador 2) jogará como X")
    return sim1, sim2

def inicializarTabuleiro():
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def definirTurno(contador, sim1, sim2):
    if contador % 2 == 0:
        jogador = 1
        return sim1, jogador
    else:
        jogador = 2
        return sim2, jogador

def posicaoValida(tabuleiro, linha, coluna):
    try:
        tabuleiro[linha][coluna]
    except IndexError:
        return False
    if tabuleiro[linha][coluna] == " ":
        return True
    else:
        return False

def jogar(tabuleiro, linha, coluna, turno):
    tabuleiro[linha][coluna] = turno

def jogadaUsuario(tabuleiro, linha, coluna, turno):
    jogar(tabuleiro, linha, coluna, turno)

def jogadaMaquina(tabuleiro, turno):
    print("Turno do computador:")
    linhaAleatoria = random.randint(0, 2)
    colunaAleatoria = random.randint(0, 2)
    while posicaoValida(tabuleiro, linhaAleatoria, colunaAleatoria) == False:
        linhaAleatoria = random.randint(0, 2)
        colunaAleatoria = random.randint(0, 2)
    jogar(tabuleiro, linhaAleatoria, colunaAleatoria, turno) 

def verificaVencedor(tabuleiro):
    for coluna in range(3):
        if tabuleiro[0][coluna] != " " and tabuleiro[0][coluna] == tabuleiro[1][coluna] and tabuleiro[1][coluna] == tabuleiro[2][coluna]:
            return True
    for linha in range(3):
        if tabuleiro[linha][0] != " " and tabuleiro[linha][0] == tabuleiro[linha][1] and tabuleiro[linha][1] == tabuleiro[linha][2]:
            return True
    if tabuleiro[0][0] != " " and tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2]:
        return True
    if tabuleiro[0][2] != " " and tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0]:
        return True
    return False

def verificaVelha(contador):
    if contador == 9:
        return True
    else:
        return False

def resultadoRodada(vitoria, empate):
    if vitoria:
        return "Vitória"
    elif empate:
        return "Empate"
    else:
        return "Em andamento"

def resultadoPartida(pontosC, pontosJ):
    if pontosC == 3 or pontosJ == 3:
        return "Acabou"
    else:
        return "Em andamento"

def imprimirMenuPrincipal():
    print("JOGO DA VELHA")
    print("1. Jogador vs. Jogador")
    print("2. Jogador vs. Computador")

def imprimirTabuleiro(tabuleiro):
    print("\n  0   1   2")
    print(f"0  {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]}")
    print("  ___|___|___")
    print(f"1  {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]}")
    print("  ___|___|___")
    print(f"2  {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]}")
    print("     |   |   ")

def imprimirResultado(jogador, turno, vitoria, empate):
    if resultadoRodada(vitoria, empate) == "Vitória":
        print(f"Vitória do jogador {jogador} ({turno})!")
    else:
        print("Empate. Deu velha!")

def imprimirPontuacao(pontosJ, pontosC):
    print(f"\nJogador: {pontosJ} ponto(s)")
    print(f"Computador: {pontosC} ponto(s)\n")

def leiaModoDeJogo():
    modo = int(input("Escolha um modo de jogo: "))
    while modo != 1 and modo != 2:
        print("Opção inválida. Digite <1> ou <2> para prosseguir.")
        modo = int(input("Escolha um modo de jogo: "))
    return modo

def leiaCoordenadaLinha(turno, jogador):
    print(f"\nTurno do jogador {jogador} ({turno})")
    return int(input("Escolha uma linha [0-2]: "))

def leiaCoordenadaColuna():
    return int(input("Escolha uma coluna [0-2]: "))

def modoJogador():
    modo = "PvP"
    repetir = "S"
    while repetir == "S":
        sim1, sim2 = definirSimbolo(modo)
        contador = 0
        tabuleiro = inicializarTabuleiro()
        while resultadoRodada(verificaVencedor(tabuleiro), verificaVelha(contador)) == "Em andamento":
                imprimirTabuleiro(tabuleiro)
                turno, jogador = definirTurno(contador, sim1, sim2)
                linha = leiaCoordenadaLinha(turno, jogador)
                coluna = leiaCoordenadaColuna()
                while posicaoValida(tabuleiro, linha, coluna) == False:
                    print("Erro: a posição inserida é inválida ou já foi preenchida. Faça uma jogada diferente.")
                    linha = leiaCoordenadaLinha(turno, jogador)
                    coluna = leiaCoordenadaColuna()
                jogadaUsuario(tabuleiro, linha, coluna, turno)
                contador += 1
        imprimirTabuleiro(tabuleiro)
        imprimirResultado(jogador, turno, verificaVencedor(tabuleiro), verificaVelha(contador))
        repetir = input("Jogar novamente? <S/N> ").upper()

def modoMaquina():
    modo = "PvC"
    pontosC = 0 
    pontosJ = 0
    while resultadoPartida(pontosC, pontosJ) == "Em andamento":
        sim1, sim2 = definirSimbolo(modo)
        contador = 0
        tabuleiro = inicializarTabuleiro()
        while resultadoRodada(verificaVencedor(tabuleiro), verificaVelha(contador)) == "Em andamento":
            imprimirTabuleiro(tabuleiro)
            turno, jogador = definirTurno(contador, sim1, sim2)
            if jogador == 1:
                linha = leiaCoordenadaLinha(turno,jogador)
                coluna = leiaCoordenadaColuna()
                while posicaoValida(tabuleiro, linha, coluna) == False:
                    print("Erro: a posição inserida é inválida ou já foi preenchida. Faça uma jogada diferente.")
                    linha = leiaCoordenadaLinha(turno,jogador)
                    coluna = leiaCoordenadaColuna()
                jogadaUsuario(tabuleiro, linha, coluna, turno)
                contador += 1
            else:
                jogadaMaquina(tabuleiro, turno)
                contador += 1
        imprimirTabuleiro(tabuleiro)
        imprimirResultado(jogador, turno, verificaVencedor(tabuleiro), verificaVelha(contador))
        if verificaVencedor(tabuleiro):
            if jogador == 1:
                pontosJ += 1
            else:
                pontosC += 1
        imprimirPontuacao(pontosJ, pontosC)
    if pontosJ > pontosC:
        print("Vitória do jogador!")
    else:
        print("Vitória do Computador!")

def main():
    imprimirMenuPrincipal()
    modo = leiaModoDeJogo()
    match modo:
        case 1:
            modoJogador()
        case 2:
            modoMaquina()
    print("\nPrograma encerrado. Obrigado por jogar!")

main()