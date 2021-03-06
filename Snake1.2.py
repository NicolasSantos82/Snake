import pygame
from random import randrange


# O pygame usa o sistema RGB (Red, Green, Blue) para definição de cores e utiliza tupla.
branco = (255, 255, 255)
preto = (0, 0, 0,)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

try:
    pygame.init()
except:
    print('O módulo pygame não foi inicializado com sucesso!')

largura = 320
altura = 280
tamanho = 10
placar = 40
velocidade_x = 0
velocidade_y = 0

# Variável que recebe parte do comando limitador de frames
relogio = pygame.time.Clock()

# Define o tamanho da tela, sendo a larguar e o altura apresentado em uma tupla
fundo = pygame.display.set_mode((largura, altura))
# Define o nome da janela
pygame.display.set_caption('Snake')


def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    fundo.blit(texto1, [x, y])


def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(fundo, preto, [XY[0], XY[1], tamanho, tamanho])


def maca(pos_x, pos_y):
    pygame.draw.rect(fundo, vermelho, [pos_x, pos_y, tamanho, tamanho])


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler o arquivo!')
    else:
        c = 0
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} pontos')
            texto(dado[0], preto, 20, 10, 50 + (20 * c))
            texto(dado[1], preto, 20, 200, 50 + (20 * c))
            c += 1
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', pontuação=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{pontuação}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print(f'Novo cadastro de {nome} com {pontuação} foi adicionado.')


def ranking():
    rankon = True
    while rankon:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        fundo.fill(branco)
        texto('Nome', preto, 40, 10, 10)
        texto('Pontuação', preto, 40, 150, 10)
        lerArquivo('Ranking.txt')
        pygame.display.update()

def menu():
    menu_on = True
    sairranking = False
    while menu_on:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if 90 <= x <= 230 and 100 <= y <= 150:
                    menu_on = False
                    return True
                if 90 <= x <= 230 and 160 <= y <= 210:
                    sairranking = ranking()
                    if not sairranking:
                        menu_on = False
                        return False
                if 90 <= x <= 230 and 220 <= y <= 270:
                    return False
        fundo.fill(branco)
        texto('SNAKE', preto, 80, 60, 30)
        pygame.draw.rect(fundo, preto, [90, 100, 140, 50])
        texto('Jogar', branco, 40, 120, 110)
        pygame.draw.rect(fundo, preto, [90, 160, 140, 50])
        texto('Ranking', branco, 40, 102, 170)
        pygame.draw.rect(fundo, preto, [90, 220, 140, 50])
        texto('Sair', branco, 40, 130, 232)
        pygame.display.update()


def jogo(naosair):
    sair = naosair
    fimdejogo = False
    pos_x = randrange(0, largura - tamanho, 10)
    pos_y = randrange(0, altura - tamanho - placar, 10)
    maca_x = randrange(0, largura - tamanho, 10)
    maca_y = randrange(0, altura - tamanho - placar, 10)
    velocidade_x = 0
    velocidade_y = 0
    CobraXY = []
    CobraComp = 1
    pontos = 0
    while sair:
        while fimdejogo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sair = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)
                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    if event.key == pygame.K_s:
                        sair = False
                        fimdejogo = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if 45 < x < 180  and 120 < y < 147:
                        sair = True
                        fimdejogo = False
                        pos_x = randrange(0, largura - tamanho, 10)
                        pos_y = randrange(0, altura - tamanho - placar, 10)
                        maca_x = randrange(0, largura - tamanho, 10)
                        maca_y = randrange(0, altura - tamanho - placar, 10)
                        velocidade_x = 0
                        velocidade_y = 0
                        CobraXY = []
                        CobraComp = 1
                        pontos = 0
                    elif 190 < x < 265 and 120 < y < 147:
                        sair = False
                        fimdejogo = False
            fundo.fill(branco)
            texto('Fim de jogo', vermelho, 50, 65, 30)
            texto('Pontuação Final: ' + str(pontos), preto, 30, 70, 80)
            pygame.draw.rect(fundo, preto, [45, 120, 135, 27])
            texto('Continuar(C)', branco, 30, 50, 125)
            pygame.draw.rect(fundo, preto, [190, 120, 75, 27])
            texto('Sair(S)', branco, 30, 195, 125)
            pygame.display.update()
        # Identifica um comando do teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho:
                    velocidade_x = -tamanho
                    velocidade_y = 0
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho:
                    velocidade_x = tamanho
                    velocidade_y = 0
                if event.key == pygame.K_UP and velocidade_y != tamanho:
                    velocidade_x = 0
                    velocidade_y = -tamanho
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho:
                    velocidade_x = 0
                    velocidade_y = tamanho
        if sair:
            # Estabelece como branco o fundo
            fundo.fill(branco)
            for c in range(0, largura, 10):
                pygame.draw.rect(fundo, preto, [c, 0, 1, altura])
            for c in range(0, altura, 10):
                pygame.draw.rect(fundo, preto, [0, c, largura, 1])
            # Faz um forma quadrilátera usando a tela, cor do objeto e a posição XY e a extenção de cada eixo.
            pos_x += velocidade_x
            pos_y += velocidade_y
            if pos_x == maca_x and pos_y == maca_y:
                maca_x = randrange(0, largura - tamanho - placar, 10)
                maca_y = randrange(0, altura - tamanho - placar, 10)
                CobraComp += 1
                pontos += 1
            if pos_x + tamanho > largura:
                pos_x = 0
            if pos_x < 0:
                pos_x = largura - tamanho
            if pos_y + 10 > altura - placar:
                pos_y = 0
            if pos_y < 0:
                pos_y = altura - tamanho - placar
            # Finaliza o jogo se o usuário atingir uma das paredes
            #if pos_x + tamanho > largura:
            #    fimdejogo = True
            #if pos_x < 0:
            #    fimdejogo = True
            #if pos_y + tamanho > altura:
            #    fimdejogo = True
            #if pos_y < 0:
            #    fimdejogo = True
            CobraInicio = []
            CobraInicio.append(pos_x)
            CobraInicio.append(pos_y)
            CobraXY.append(CobraInicio)
            if len(CobraXY) > CobraComp:
                del CobraXY[0]
            for bloco in CobraXY:
                c = CobraXY.count(bloco)
                if c == 2:
                    fimdejogo = True
            pygame.draw.rect(fundo, preto, [0, altura - placar, largura, placar])
            texto('Pontuação: ' + str(pontos), branco, 20, 10, altura - 30)
            cobra(CobraXY)
            maca(maca_x, maca_y)
            # Atualiza a tela em exibição
            pygame.display.update()
            # LIMITA o loop a 15 frames por segundo
            relogio.tick(15)


escolha = menu()
jogo(escolha)
# Encerra o sistema
pygame.quit()
