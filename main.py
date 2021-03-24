# Pyncake Editor
# Created by Danix. Coding by Danix, CarrotOnCanvas and METGaming
# Artwork by Danix and METGaming
# Font "Silver" by Poppy Works
# Discord Rich Presence system "Pypresence" by qwertyquerty

import pygame, sys, pypresence, json
import math, random
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
        colors = Colors()

        config = {
           "rich presence": True
        }
        
        try:
            config = json.load(open("Data/config.pyncake", "r"))
        except FileNotFoundError:
            json.dump(config, open("Data/config.pyncake", "w"))
            config = json.load(open("Data/config.pyncake", "r"))
    
    class PartSYS:
        def __init__(self):
            self.particles = []
        def create_particles(self, loc, size, amount,):
            for r in range(0, amount):
                self.particles.append([loc[0], loc[1], \
                        random.randint(size/2, size), random.uniform(0.00, 359.00)])
        def update_particles(self, speed, decay):
            particles_to_remove = []

            for p in self.particles:
                p[0] += math.cos(math.radians(p[3])) * speed
                p[1] -= math.sin(math.radians(p[3])) * speed

                p[2] -= decay
                if p[2] < 0:
                    particles_to_remove.append(p)
                p[3] += 0

            for pR in particles_to_remove:
                self.particles.remove(pR)
        def draw(self, window):
            for p in self.particles:
                pygame.draw.circle(window, app.data.colors.white, (p[0], p[1]), p[2])
    
    PartSYS = PartSYS()
    
    def __init__(self):
        self.window = pygame.display.set_mode(self.metadata.window_size, pygame.NOFRAME)
        pygame.display.set_caption(self.metadata.app_name)
        pygame.display.set_icon(self.metadata.app_icon)
        self.running = True

        self.font = pygame.font.Font(self.data.fonts_dir + "Silver.ttf", 30)

        self.exit = self.font.render("X", True, self.data.colors.white)

        self.cursor = pygame.image.load(self.data.graphics_dir + "cursor.png")
        
        if self.data.config["rich presence"]:
            try:
                self.RP = pypresence.Presence("811677670718570536")
                self.RP.connect()
                self.RP.update(large_image = "appicon", large_text = "Pyncake Editor", state = "In editor")
            except pypresence.exceptions.InvalidPipe:
                pass
        
        pygame.mouse.set_visible(False)
        while self.running:
            self.window.fill((0,0,0))
            self.data.mouse_pos = pygame.mouse.get_pos()
            # Blit screen
            self.window.blit(self.exit, (912, 1))
            self.down_bar = pygame.draw.rect(self.window, self.data.colors.pancake, (0, 730, 950, 20))
            self.left_bar = pygame.draw.rect(self.window, self.data.colors.blue, (0, 0, 45, 750))
            self.up_bar = pygame.draw.rect(self.window, self.data.colors.grey, (0, 0, 1000, 25))
            self.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
            self.window.blit(self.metadata.app_logo, (150, 150))
            # Exit blitting code
            if self.exitbutton.collidepoint(self.data.mouse_pos):
                self.exitbutton = pygame.draw.rect(self.window, self.data.colors.red, (880, 0, 70, 25))
                self.window.blit(self.exit, (912, 1))
            else:
                self.exitbutton = pygame.draw.rect(self.window, self.data.colors.grey, (880, 0, 70, 25))
                self.window.blit(self.exit, (912, 1))
            # Blit and Update Particles (you can adjust the varis here)
            self.PartSYS.draw(self.window)
            self.PartSYS.update_particles(2.5, 0.5)
            # Draw mouse
            self.window.blit(self.cursor, (self.data.mouse_pos))
            
            for self.event in pygame.event.get():
                if self.event.type == MOUSEBUTTONDOWN:
                    # Create particles on click (you can adjust the varis here)
                    self.PartSYS.create_particles([self.data.mouse_pos[0], self.data.mouse_pos[1]], 12, 12)
                    if self.event.button == 1:
                        if self.exitbutton.collidepoint(self.data.mouse_pos):
                            pygame.quit()
                            sys.exit()

            pygame.display.update()

app()
