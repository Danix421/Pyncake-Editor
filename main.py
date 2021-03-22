# Pyncake Editor
# Coded by Danix, CarrotOnCanvas and METGaming
# Artwork by Danix
# Font "Silver" by Poppy Works
# Discord Rich Presence system "Pypresence" by qwertyquerty

import pygame, sys, pypresence, json
from pygame.locals import *
from Data.colors import Colors

pygame.init()

class app:
    class metadata:
        screen = pygame.display.Info()
        app_name = "Pyncake Editor"
        app_icon = pygame.image.load("app_icon.png")
        app_logo = pygame.image.load("Data/Graphics/pyncake.png")
        window_size = (950, 750)
    
    class data:
        data_dir = "Data/"
        graphics_dir = data_dir + "Graphics/"
        fonts_dir = data_dir + "Fonts/"
        font = pygame.font.Font(fonts_dir + "Silver.ttf", 30)
        colors = Colors()
        exit = font.render("X", True, colors.white)
        
        data = {
           "Packages" : "Script"
        }
        
        with open('project.json', 'w+') as project_file:
            json.dump(data, project_file)
        
    def __init__(self):
        self.window = pygame.display.set_mode(self.metadata.window_size, pygame.NOFRAME)
        pygame.display.set_caption(self.metadata.app_name)
        pygame.display.set_icon(self.metadata.app_icon)
        self.running = True

        self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
        pygame.mouse.set_visible(False)
        while self.running:
            self.window.fill((0,0,0))
            self.data.mouse_pos = pygame.mouse.get_pos()
            self.window.blit(self.data.exit, (912, 1))
            self.data.down_bar = pygame.draw.rect(self.window, self.data.colors.pancake, (0, 730, 950, 20))
            self.data.left_bar = pygame.draw.rect(self.window, self.data.colors.blue, (0, 0, 45, 750))
            self.data.up_bar = pygame.draw.rect(self.window, self.data.colors.grey, (0, 0, 1000, 25))
            self.window.blit(self.metadata.app_logo, (150, 150))
            if self.data.exitbutton.collidepoint(self.data.mouse_pos):
                self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.red, (880, 0, 70, 25))
                self.window.blit(self.data.exit, (912, 1))
            else:
                self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
                self.window.blit(self.data.exit, (912, 1))
            pygame.draw.rect(self.window, (0,255,255), (self.data.mouse_pos[0], self.data.mouse_pos[1], 20,20))
            for self.event in pygame.event.get():
                if self.event.type == MOUSEBUTTONDOWN:
                    if self.event.button == 1:
                        if self.data.exitbutton.collidepoint(self.data.mouse_pos):
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

app()
