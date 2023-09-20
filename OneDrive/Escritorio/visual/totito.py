import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

open = True

juego=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\totito.png")
simbolo1=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\imagenes\pngx.png")
simbolo2=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\imagenes\pngo.png")

# Configuración de la ventana
WINDOW_SIZE = (720, 720)
CELL_SIZE = WINDOW_SIZE[0] // 3, WINDOW_SIZE[1] // 3
WIN_LINE_WIDTH = 5
BACKGROUND_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (0, 0, 255)
CROSS_COLOR = (255, 0, 0)

# Inicializar el tablero vacío
board = [['' for _ in range(3)] for _ in range(3)]

screen.fill("black")

def menu():

    open = True

    while open:
        


        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.quit or keys[pygame.K_ESCAPE]:
                running = False

            # foto instrucciones
            instrucciones=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\imagenes\instru.png")
            screen.blit(instrucciones,((0,0),(1280,720)))
            
            pygame.draw.line(screen, "white" , (screen.get_width() / 4,screen.get_height() / 2), (screen.get_width() / 4,screen.get_height() / 11))
            pygame.draw.line(screen, "white" , (screen.get_width() / 3,screen.get_height() / 2), (screen.get_width() / 1.5 * .5,screen.get_height() / 11))
            pygame.draw.line(screen, "white" , (screen.get_width() / 7,screen.get_height() / 2.7), (screen.get_width() / 2.4,screen.get_height() / 2.7))
            pygame.draw.line(screen, "white" , (screen.get_width() / 7,screen.get_height() / 4.7), (screen.get_width() / 2.4,screen.get_height() / 4.7))

            # boton para empezar
            button=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\start.png")
            screen.blit(button,((screen.get_width() / 1.8,screen.get_height() / 6 ),(screen.get_width() / 2,screen.get_height() / 6)))

            if keys[pygame.K_x]:
                open=False



            pygame.display.flip()
            clock.tick(60)
            pygame.quit

# Función para dibujar el tablero en la ventana
    def draw_board(screen):
        screen.fill(BACKGROUND_COLOR)

        for i in range(1, 3):
            pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE[0] * i, 0), (CELL_SIZE[0] * i, WINDOW_SIZE[1]), WIN_LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE[1] * i), (WINDOW_SIZE[0], CELL_SIZE[1] * i), WIN_LINE_WIDTH)

        for row in range(3):
            for col in range(3):
                cell_content = board[row][col]
                if cell_content == 'X':
                    draw_cross(screen, row, col)
                elif cell_content == 'O':
                    draw_circle(screen, row, col)

    # Función para dibujar una cruz en una celda específica
    def draw_cross(screen, row, col):
        x1 = col * CELL_SIZE[0] + WIN_LINE_WIDTH
        y1 = row * CELL_SIZE[1] + WIN_LINE_WIDTH
        x2 = (col + 1) * CELL_SIZE[0] - WIN_LINE_WIDTH
        y2 = (row + 1) * CELL_SIZE[1] - WIN_LINE_WIDTH
        pygame.draw.line(screen, CROSS_COLOR, (x1, y1), (x2, y2), WIN_LINE_WIDTH)
        pygame.draw.line(screen, CROSS_COLOR, (x1, y2), (x2, y1), WIN_LINE_WIDTH)

    # Función para dibujar un círculo en una celda específica
    def draw_circle(screen, row, col):
        x = col * CELL_SIZE[0] + CELL_SIZE[0] // 2
        y = row * CELL_SIZE[1] + CELL_SIZE[1] // 2
        radius = CELL_SIZE[0] // 2 - WIN_LINE_WIDTH
        pygame.draw.circle(screen, CIRCLE_COLOR, (x, y), radius, WIN_LINE_WIDTH)
    
    def check_win():
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '':
                return True


        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '':
                return True

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
            return True

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
            return True

        return False

    # Función para verificar si el tablero está lleno y hay un empate
    def check_draw():
        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    return False
        return True

    def main():
        screen = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption("Juego del Gato")
        clock = pygame.time.Clock()

        player_turn = 'X'

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not check_win() and not check_draw():
                        x, y = event.pos
                        row, col = y // CELL_SIZE[1], x // CELL_SIZE[0]

                        if board[row][col] == '':
                            board[row][col] = player_turn
                            if player_turn == 'X':
                                player_turn = 'O'
                            else:
                                player_turn = 'X'

            draw_board(screen)
            pygame.display.flip()
            clock.tick(60)

    if __name__ == "__main__":
        main()


        pygame.display.flip()
        clock.tick(60)
    

menu()

pygame.display.flip()
clock.tick(60)


pygame.quit()