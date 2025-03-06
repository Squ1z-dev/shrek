from tkinter import *
import  pygame
import time
from  tkinter import messagebox

Tk().wm_withdraw()

"""icon  = pygame.image.load('malware.png')"""

pygame.init()
screen = pygame.display.set_mode((850,   150))
screen.fill((0, 0, 0))

pygame.display.set_caption("WARNING!!!")
font = pygame.font.SysFont("Lucida Console", 20)
label = font.render("YOU DOWNLOAD VIRUS", 1, (12, 140, 0, 1))
screen.blit(label, (50,  50))
"""pygame.display.set_icon(icon)"""
pygame.display.update( )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            time.sleep(0.10)
            screen = pygame.display.set_mode((850,150))
            pygame.display.set_caption("IMPORTANT!!!")
            pygame.display.set_icon(icon)
            messagebox.showerror("LOL", "We are steal your DATA")

        screen.fill((0, 0, 0,))
        screen.blit(label, (50, 50))
        pygame.display.update()
