import pygame
from network import Network

width = 500
height =500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("client")


def redrawWindow(player, player2):
    win.fill((255,255,255))
    player2.draw(win)
    player.draw(win)

    pygame.display.update()
    
def main():
    run= True
    n= Network()
    player = n.getP()
    
    while run:
        p2 = n.send(player)
        p2.update()
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                pygame.quit()
                
            player.move()    
            redrawWindow(player,p2)
            
main()