import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:    
            if event.type == pygame.KMOD_NONE:
            # forma de hashtag
                pygame.draw.line(screen, "white" , (screen.get_width() / 4,screen.get_height() / 2), (screen.get_width() / 4,screen.get_height() / 11))
                pygame.draw.line(screen, "white" , (screen.get_width() / 3,screen.get_height() / 2), (screen.get_width() / 1.5 * .5,screen.get_height() / 11))
                pygame.draw.line(screen, "white" , (screen.get_width() / 7,screen.get_height() / 2.7), (screen.get_width() / 2.4,screen.get_height() / 2.7))
                pygame.draw.line(screen, "white" , (screen.get_width() / 7,screen.get_height() / 4.7), (screen.get_width() / 2.4,screen.get_height() / 4.7))
    
                # foto instrucciones
                instrucciones=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\instrucciones.png")
                screen.blit(instrucciones,((screen.get_width() / 7,screen.get_height() / 1.8 ),(screen.get_width() / 4,screen.get_height() / 6)))

                # boton para empezar
                instrucciones=pygame.image.load(r"C:\Users\cesar\OneDrive\Escritorio\checha\start.png")
                screen.blit(instrucciones,((screen.get_width() / 1.8,screen.get_height() / 6 ),(screen.get_width() / 2,screen.get_height() / 6)))


    pygame.display.flip()
    clock.tick(60)


pygame.quit()