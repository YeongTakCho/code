from player import Player
import pygame
from network import Network

width = 500
height =500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("client")


def read_pos(str): # "45,67" -> (45,67)
    str= str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup): # (45,67) -> "45,67"
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()
    
def main():
    run= True
    n= Network()
    startPos= read_pos(n.get_pos())
    
    p = Player(startPos[0], startPos[1], 100, 100, (0,255,0))
    p.draw(win)
    p2 = Player(startPos[0], startPos[1], 100, 100, (0,0,255))
    
    while run:
        p2Pos= read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2Pos[0]
        p2.y = p2Pos[1]
        p2.update()
        
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                run = False
                pygame.quit()
            p.move()    
            redrawWindow(p,p2)
            
main()