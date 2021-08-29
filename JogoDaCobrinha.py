import random as rd
from sys import exit
import emoji
import pygame
from pygame.locals import *

#C0NSTANTES
WINDOW_SIZE = (640, 480)
PIXEL_SIZE = 10

#VÁRIAVEIS
pontos = 0
high_score = 0
ticks = 10
nivel = 'Fácil'

#Inicializa o pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)#Cria um objeto chamado 'screen' que vai receber o formato da tela
pygame.display.set_caption(emoji.emojize("Jogo da Cobrinha :snake:", use_aliases=True))#Colocando o nome da janela

#Configurações EXTRAS do JOGO:
fonte = pygame.font.SysFont('ComicsSans', 21, True, False)
background_image = pygame.image.load('images/background-image.dib')

clock = pygame.time.Clock()

gameloop = True
song1 = 'songs/BoxCat Games - Inspiration.mp3'
soundCoin = pygame.mixer.Sound('songs/smw_coin.wav')
soundDeath = pygame.mixer.Sound('songs/death_sound.wav')
pygame.mixer.music.set_volume(0.15)
background_music = pygame.mixer.music
background_music.load(song1)
pygame.mixer.music.play(-1)

#Configurações das PEDRAS
stone_image = pygame.image.load('images/stone_image.png')
stone_image_use = pygame.transform.scale(stone_image, (PIXEL_SIZE, PIXEL_SIZE))
stone_pos1 = [(320, 130), (320, 140), (320, 150), (320, 160)]
stone_pos2 = [(120, 420), (120, 430), (120, 440), (120, 450), (120, 460)]
stone_pos3 = [(250, 300), (260, 300), (270, 300), (280, 300), (290, 300)]
stone_pos4 = [(550, 90), (560, 90), (570, 90), (580, 90)]
stone_pos5 = [(70, 220), (80, 220), (90, 220), (100, 220), (110, 220)]
stone_pos6 = [(590, 330), (590, 340), (590, 350), (590, 360), (590, 370)]
stone_pos7 = [(90, 20), (90, 30), (90, 40), (90, 50), (90, 60)]

#Função para colisão com o próprio corpo
def collision(pos1, pos2):
    return pos1 == pos2
#Função para colisão na parede
def off_limites(pos):
    if 0 <= pos[0] < WINDOW_SIZE[0] and 0 <= pos[1] < WINDOW_SIZE[1]:
        return False
    else:
        return True
#Checar as posições X e Y
def checkX(x1, x2):
    return x1 == x2
def checkY(y1, y2):
    return y1 == y2

#Função para Maçã respawnar em algum lugar aleatótio da tela
def random_on_grid():
    while True:
        x1 = rd.randint(20, 600)
        y1 = rd.randint(20, 440)
        x = (x1 // PIXEL_SIZE) * PIXEL_SIZE
        y = (y1 // PIXEL_SIZE) * PIXEL_SIZE
        #Colisão com a PEDRA
        pode = True

        #Pedra 1
        if checkX(320 , x) and checkY(130 , y):
            pode = False
        if checkX(320, x) and checkY(140, y):
            pode = False
        if checkX(320, x) and checkY(150, y):
            pode = False
        if checkX(320, x) and checkY(160, y):
            pode = False
        # Pedra 2
        if checkX(120, x) and checkY(420, y):
            pode = False
        if checkX(120, x) and checkY(430, y):
            pode = False
        if checkX(120, x) and checkY(440, y):
            pode = False
        if checkX(120, x) and checkY(450, y):
            pode = False
        if checkX(120, x) and checkY(460, y):
            pode = False
        # Pedra 3
        if checkX(250, x) and checkY(300, y):
            pode = False
        if checkX(260, x) and checkY(300, y):
            pode = False
        if checkX(270, x) and checkY(300, y):
            pode = False
        if checkX(280, x) and checkY(300, y):
            pode = False
        if checkX(290, x) and checkY(300, y):
            pode = False
        # Pedra 4
        if checkX(550, x) and checkY(90, y):
            pode = False
        if checkX(560, x) and checkY(90, y):
            pode = False
        if checkX(570, x) and checkY(90, y):
            pode = False
        if checkX(580, x) and checkY(90, y):
            pode = False
        # Pedra 5
        if checkX(70, x) and checkY(220, y):
            pode = False
        if checkX(80, x) and checkY(220, y):
            pode = False
        if checkX(90, x) and checkY(220, y):
            pode = False
        if checkX(100, x) and checkY(220, y):
            pode = False
        if checkX(110, x) and checkY(220, y):
            pode = False
        # Pedra 6
        if checkX(590, x) and checkY(330, y):
            pode = False
        if checkX(590, x) and checkY(340, y):
            pode = False
        if checkX(590, x) and checkY(350, y):
            pode = False
        if checkX(590, x) and checkY(360, y):
            pode = False
        if checkX(590, x) and checkY(370, y):
            pode = False
        # Pedra 7
        if checkX(90, x) and checkY(20, y):
            pode = False
        if checkX(90, x) and checkY(30, y):
            pode = False
        if checkX(90, x) and checkY(40, y):
            pode = False
        if checkX(90, x) and checkY(50, y):
            pode = False
        if checkX(90, x) and checkY(60, y):
            pode = False

        if pode == True:
            break
    return x, y

#FUNÇÃO PARA DA UM RESTART NO JOGO
def restart_game():
    global snake_pos
    global apple_pos
    global snake_direction
    global quant_ticks
    global pontos
    global apple_cont
    global nivel
    global ticks

    snake_pos = [(250, 50), (260, 50), (270, 50)]
    snake_direction = K_a
    apple_pos = random_on_grid()
    quant_ticks = 0
    apple_cont = 0
    pontos = 0
    nivel = 'Fácil'
    ticks = 10


#FUNÇÃO PARA MUDAR DE LEVEL
def change_level():
    global ticks
    global pontos
    global nivel
    if pontos >= 15 and pontos < 30:
        ticks = 12
        nivel = 'Médio'
    elif pontos >= 30 and pontos < 50:
        ticks = 15
        nivel = 'Difícil'
    elif pontos >= 50:
        ticks = 18
        nivel = 'Lendário'
    return ticks, nivel

#FUNÇÃO PARA PAUSAR O JOGO
def config():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    paused = False


        background_image_config = pygame.image.load('images/screen_config.png')
        background_image_config = pygame.transform.scale(background_image_config, WINDOW_SIZE)
        screen.blit(background_image_config, (0, 0))
        pygame.display.flip()
        clock.tick(5)


#FUNÇÃO PARA PAUSAR O JOGO
def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_r:
                    restart_game()
                    paused = False
                elif event.key == pygame.K_g:
                    config()
                elif event.key == pygame.K_s:
                    pygame.quit()
                    quit()
        background_image_pause = pygame.image.load('images/screen_pause.png')
        background_image_pause = pygame.transform.scale(background_image_pause, WINDOW_SIZE)
        screen.blit(background_image_pause, (0, 0))
        pygame.display.flip()
        clock.tick(5)

#Configurações da Cobra
snake_pos = [(250, 50), (260, 50), (270, 50)]
head_snake_image = pygame.image.load('images/head_snake.png')
head_snake_image_use = pygame.transform.scale(head_snake_image, (PIXEL_SIZE, PIXEL_SIZE))
body_snake_image = pygame.image.load('images/body_snake.png')
body_snake_image_use = pygame.transform.scale(body_snake_image, (PIXEL_SIZE, PIXEL_SIZE))
foot_snake_image = pygame.image.load('images/foot_snake.png')
foot_snake_image_use = pygame.transform.scale(foot_snake_image, (PIXEL_SIZE, PIXEL_SIZE))
snake_direction = K_a

#Configurações da Maçã
apple_image = pygame.image.load('images/apple-image.png')
apple_image_use = pygame.transform.scale(apple_image, (PIXEL_SIZE, PIXEL_SIZE))
apple_pos = random_on_grid()
apple_cont = 0

#Configurações da Melancia
watermelon_image = pygame.image.load('images/watermelon-image.png')
watermelon_image_use = pygame.transform.scale(watermelon_image, (PIXEL_SIZE, PIXEL_SIZE))
watermelon_pos = random_on_grid()
watermelon_cont = 0

quant_ticks = 0

while gameloop:

    mensagem = f'HIGH SCORE: {high_score}'
    mensagem1 = f'SCORE: {pontos}'
    mensagem2 = f'LEVEL: {nivel}'
    mensagem3 = 'Aperte ENTER para Pausar'
    texto_formatado = fonte.render(mensagem, False, (255,255,255))
    texto_formatado1 = fonte.render(mensagem1, False, (255, 255, 255))
    texto_formatado2 = fonte.render(mensagem2, False, (255, 255, 255))
    texto_formatado3 = fonte.render(mensagem3, False, (255, 255, 255))

    clock.tick(ticks)

    #BLIT DA IMAGEM DE FUNDO
    screen.blit(background_image, (0, 0))

    #BLIT TEXTO FORMATADO
    screen.blit(texto_formatado, (490, 20))
    screen.blit(texto_formatado1, (490, 45))
    screen.blit(texto_formatado2, (490, 70))
    screen.blit(texto_formatado3, (10, 10))

    for event in pygame.event.get():
        #Botão de SAIR!
        if event.type == QUIT:
            pygame.quit()
            exit()
        #Botão para MOVER!
        elif event.type == KEYDOWN:
            if event.key in [K_a, K_s, K_d, K_w]:
                snake_direction = event.key
            #Botão para PAUSAR!
            elif event.key == pygame.K_RETURN:
                pause()


    #BLIT da PEDRA
    for pos in stone_pos1:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos2:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos3:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos4:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos5:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos6:
        screen.blit(stone_image_use, (pos))
    for pos in stone_pos7:
        screen.blit(stone_image_use, (pos))

    #BLIT da MAÇÃ
    screen.blit(apple_image_use,(apple_pos))
    apple_image_use.blit(apple_image_use, (apple_pos))

    #BLIT da COBRA
    screen.blit(head_snake_image_use, snake_pos[0])
    for pos in range(1, len(snake_pos)-1):
            screen.blit(body_snake_image_use, snake_pos[pos])
    screen.blit(foot_snake_image_use, snake_pos[len(snake_pos)-1])

    #COMER MAÇÃ
    if collision(apple_pos, snake_pos[0]):
        soundCoin.play()
        apple_cont += 1
        pontos += 1
        snake_pos.append((0, 0))
        apple_pos = random_on_grid()

    #BLIT DA MELANCIA
    if apple_cont >= 10:
        screen.blit(watermelon_image_use,(watermelon_pos))
        watermelon_image_use.blit(watermelon_image_use, (watermelon_pos))
        quant_ticks += 1
        if ticks == 10 and quant_ticks >= 67:
            quant_ticks = 0
            watermelon_pos = random_on_grid()
        if ticks == 12 and quant_ticks >= 70:
            quant_ticks = 0
            watermelon_pos = random_on_grid()
        if ticks == 16 and quant_ticks >= 76:
            quant_ticks = 0
            watermelon_pos = random_on_grid()
        if ticks == 22 and quant_ticks >= 85:
            quant_ticks = 0
            watermelon_pos = random_on_grid()
        #COMER MELANCIA
        if collision(watermelon_pos, snake_pos[0]):
            soundCoin.play()
            watermelon_cont += 1
            pontos += 3
            snake_pos.append((0, 0))
            quant_ticks = 0
            watermelon_pos = random_on_grid()

    #MUNDANÇA DE NÍVEL
    change_level()

    #COLISÃO COM O PRÓPRIO CORPO
    if snake_pos.count(snake_pos[0]) > 1:
        soundDeath.play()
        if pontos >= high_score:
            high_score = pontos
        restart_game()

    #CORPO ACOMPANHAR A CABEÇA
    for i in range(len(snake_pos)-1, 0, -1):
        #Colisão com o PRÓPRIO CORPO
        if collision(snake_pos[0], snake_pos[i]):#List index out in range!
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
        else:
            snake_pos[i] = snake_pos[i-1]

    #Colisão com a PEDRA
    for pos in stone_pos1:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
    for pos in stone_pos2:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
    for pos in stone_pos3:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
    for pos in stone_pos4:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
    for pos in stone_pos5:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()
    for pos in stone_pos6:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()

    for pos in stone_pos7:
        if collision((pos), snake_pos[0]):
            soundDeath.play()
            if pontos >= high_score:
                high_score = pontos
            restart_game()

    # Colisão com a PAREDE
    if off_limites(snake_pos[0]):
        soundDeath.play()
        if pontos >= high_score:
            high_score = pontos
        restart_game()

    # MOVIMENTAÇÃO DA CABEÇA
    if snake_direction == K_w:  # MOVER PARA CIMA
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] - PIXEL_SIZE)
    elif snake_direction == K_s:  # MOVER PARA BAIXO
        snake_pos[0] = (snake_pos[0][0], snake_pos[0][1] + PIXEL_SIZE)
    elif snake_direction == K_a:  # MOVER PARA ESQUERDA
        snake_pos[0] = (snake_pos[0][0] - PIXEL_SIZE, snake_pos[0][1])
    elif snake_direction == K_d:  # MOVER PARA DIREITA
        snake_pos[0] = (snake_pos[0][0] + PIXEL_SIZE, snake_pos[0][1])

    pygame.display.update()
