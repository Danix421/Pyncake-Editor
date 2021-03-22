# Pyncake Editor
# Made by Danix and CarrotOnCanvas
# Font "Silver" by Poppy Works

import pygame, sys, pypresence
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
        
        with open('project.txt','w') as project_file:
            json.dump(data,project_file)
            
        with open('project.txt') as project_file:
            data = json.load(project_file)
            for entry in data_items:
                print(entry)
        
    def __init__(self):
        self.window = pygame.display.set_mode(self.metadata.window_size, pygame.NOFRAME)
        pygame.display.set_caption(self.metadata.app_name)
        pygame.display.set_icon(self.metadata.app_icon)
        self.running = True

        self.RP = pypresence.Presence("811677670718570536")
        self.RP.connect()
        self.RP.update(large_image = "appicon", state = "In editor", large_text = "Pyncake Editor")

        self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
        self.window.blit(self.data.exit, (912, 1))
        self.data.down_bar = pygame.draw.rect(self.window, self.data.colors.pancake, (0, 730, 950, 20))
        self.data.left_bar = pygame.draw.rect(self.window, self.data.colors.blue, (0, 0, 45, 750))
        self.data.up_bar = pygame.draw.rect(self.window, self.data.colors.grey, (0, 0, 1000, 25))

        self.window.blit(self.metadata.app_logo, (150, 150))

        while self.running:
            self.data.mouse_pos = pygame.mouse.get_pos()
            if self.data.exitbutton.collidepoint(self.data.mouse_pos):
                self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.red, (880, 0, 70, 25))
                self.window.blit(self.data.exit, (912, 1))
            else:
                self.data.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
                self.window.blit(self.data.exit, (912, 1))
            for self.event in pygame.event.get():
                if self.event.type == MOUSEBUTTONDOWN:
                    if self.event.button == 1:
                        if self.data.exitbutton.collidepoint(self.data.mouse_pos):
                            pygame.quit()
                            sys.exit()
            pygame.display.update()

app()
