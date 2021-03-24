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
    
    class data:
        app_name = "Pyncake Editor"
        app_icon = pygame.image.load("app_icon.png")
        app_logo = pygame.image.load("Data/Graphics/pyncake.png")
        window_size = (950, 750)

        config = {
           "rich presence": True
        }
        
        try:
            config = json.load(open("Data/config.pyncake", "r"))
        except FileNotFoundError:
            json.dump(config, open("Data/config.pyncake", "w"))
            config = json.load(open("Data/config.pyncake", "r"))
    
    colors = Colors()

    font = pygame.font.Font("Data/Fonts/Silver.ttf", 30)

    cursor = pygame.image.load("Data/Graphics/cursor.png")

    window = pygame.display.set_mode(data.window_size, pygame.NOFRAME)

    exit = font.render("X", True, colors.white)
    exitbutton = pygame.draw.rect(window, colors.grey, (880, 0, 70, 25))
    
    class Editor:
        user_text = ''
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[0:-1]
                    else:
                        user_text += event.unicode
            text_surface = font.render(user_text,True,(255,255,255))
            screen.blit(text_surface,(0,0))
    
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
                pygame.draw.circle(window, app.colors.white, (p[0], p[1]), p[2])
    
    class ErrorScreen:
        def __init__(self):
            self.fallen_pancakes = pygame.image.load("Data/Graphics/fallen_over_pancakes.png")
            self.font = pygame.font.Font("Data/Fonts/FutilePro.ttf", 40)
            self.e_texts = []
        def draw(self, window, error):
            self.e_texts.append([self.font.render("Ops! The editor ran into an error", True, app.colors.white), [60,100]])
            self.e_texts.append([self.font.render("Here's the error code. Send it to the devs.", True, app.colors.white), [60, 170]])
            self.e_texts.append([self.font.render(error[0:35], True, app.colors.red), [60, 250]])
            self.e_texts.append([self.font.render(error[35:len(error)], True, app.colors.red), [60, 320]])
            pygame.mouse.set_visible(False)
            while True:
                app.data.mouse_pos = pygame.mouse.get_pos()
                # Blit the screen
                window.fill(app.colors.black)
                window.blit(self.fallen_pancakes, (60,450))
                pygame.draw.rect(window, app.colors.blue, (0, 0, 45, 750))
                pygame.draw.rect(window, app.colors.grey, (0, 0, 1000, 25))
                pygame.draw.rect(window, app.colors.red, (45, 225, 1000, 3))
                for t in self.e_texts:
                    window.blit(t[0], t[1])
                if app.exitbutton.collidepoint(app.data.mouse_pos):
                    app.exitbutton = pygame.draw.rect(window, app.colors.red, (880, 0, 70, 25))
                    window.blit(app.exit, (912, 1))
                else:
                    app.exitbutton = pygame.draw.rect(window, app.colors.grey, (880, 0, 70, 25))
                    window.blit(app.exit, (912, 1))
                # Blit and Update Particles (you can adjust the varis here)
                app.PartSYS.draw(window)
                app.PartSYS.update_particles(2, 0.5)
                # Draw mouse
                window.blit(app.cursor, (app.data.mouse_pos))
                for self.event in pygame.event.get():
                    if self.event.type == MOUSEBUTTONDOWN:
                        # Create particles on click (you can adjust the varis here)
                        app.PartSYS.create_particles([app.data.mouse_pos[0], app.data.mouse_pos[1]], 12, 12)
                        if self.event.button == 1:
                            if app.exitbutton.collidepoint(app.data.mouse_pos):
                                pygame.quit()
                                sys.exit()
                pygame.display.update()
    
    PartSYS = PartSYS()
    ErrorScreen = ErrorScreen()

    def __init__(self):
        try:
            pygame.display.set_caption(self.data.app_name)
            pygame.display.set_icon(self.data.app_icon)
            self.running = True

            if self.data.config["rich presence"]:
                try:
                    self.RP = pypresence.Presence("811677670718570536")
                    self.RP.connect()
                    self.RP.update(large_image = "appicon", large_text = "Pyncake Editor", state = "In editor")
                except pypresence.exceptions.InvalidPipe:
                    pass
        
            pygame.mouse.set_visible(False)

            while self.running:
                self.window.fill(self.colors.black)
                self.data.mouse_pos = pygame.mouse.get_pos()
                # Blit screen
                self.window.blit(self.exit, (912, 1))
                pygame.draw.rect(self.window, self.colors.pancake, (0, 730, 950, 20))
                pygame.draw.rect(self.window, self.colors.blue, (0, 0, 45, 750))
                pygame.draw.rect(self.window, self.colors.grey, (0, 0, 1000, 25))
                self.window.blit(self.data.app_logo, (150, 150))
                # Exit blitting code
                if self.exitbutton.collidepoint(self.data.mouse_pos):
                    self.exitbutton = pygame.draw.rect(self.window, self.colors.red, (880, 0, 70, 25))
                    self.window.blit(self.exit, (912, 1))
                else:
                    self.exitbutton = pygame.draw.rect(self.window, self.colors.grey, (880, 0, 70, 25))
                    self.window.blit(self.exit, (912, 1))
                # Blit and Update Particles (you can adjust the varis here)
                self.PartSYS.draw(self.window)
                self.PartSYS.update_particles(2, 0.5)
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
        except Exception as error:
            self.ErrorScreen.draw(self.window, str(error))

app()
