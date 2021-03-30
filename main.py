# Pyncake Editor
# Created and coded by Danix.
# Artwork, logo and icon design by Danix.
# Contributions by METGaming and CarrotOnCanvas
# Font "Silver" by Poppy Works
# Font "Futile Pro" by Eeve Somepx
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
           "rich presence": True,
           "particles": False
        }
        
        try:
            config = json.load(open("Data/config.pyncake", "r"))
        except FileNotFoundError:
            json.dump(config, open("Data/config.pyncake", "w"))
            config = json.load(open("Data/config.pyncake", "r"))
    
    colors = Colors()

    font = pygame.font.Font("Data/Fonts/Silver.ttf", 30)

    cursor = pygame.image.load("Data/Graphics/cursor.png")

    # Current app place where you are. Default: "Editor"
    currentState = "Editor"

    window = pygame.display.set_mode(data.window_size, pygame.NOFRAME)

    RP = pypresence.Presence("811677670718570536")
    
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
            app.exit = app.font.render("X", True, app.colors.white)
            app.exitbutton = pygame.draw.rect(window, app.colors.grey, (880, 0, 70, 25))
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
                pygame.draw.rect(window, app.colors.left_bar, (0, 0, 45, 750))
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
                        # Create particles on click, if they are active (you can adjust the varis here)
                        if app.data.config["particles"]:
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
                    self.RP.connect()
                    self.RP.active = True
                except pypresence.exceptions.InvalidPipe:
                    self.RP.active = False
            else:
                self.RP.active = False
            
            self.exit = self.font.render("X", True, self.colors.white)
            self.exitbutton = pygame.draw.rect(self.window, self.colors.grey, (880, 0, 70, 25))
        
            pygame.mouse.set_visible(False)

            self.user_code = [""]
            self.user_code_lines = 1
            self.user_code_saved = False

            self.app_title = self.font.render(self.data.app_name, True, self.colors.white)

            if self.RP.active:
                self.RP.update(large_image = "coding", large_text = "Coding", small_image = "appicon", small_text = "Pyncake Editor",state = "In editor")

            while self.running:
                self.window.fill(self.colors.black)
                self.data.mouse_pos = pygame.mouse.get_pos()
                # Blit screen
                if self.currentState == "Editor":
                    self.user_code_y = 10
                    for lines in range(self.user_code_lines):
                        self.user_code_y += 30
                        self.user_code_text = self.font.render(self.user_code[lines], True, self.colors.white)
                        self.user_code_text_rect = self.user_code_text.get_rect()
                        self.user_code_text_rect.x = 100
                        self.user_code_text_rect.y = self.user_code_y
                        self.user_code_currentLine = self.font.render(str(lines + 1), True, self.colors.white)
                        self.user_code_currentLine_rect = self.user_code_currentLine.get_rect()
                        self.user_code_currentLine_rect.x = 70
                        self.user_code_currentLine_rect.y = self.user_code_y
                        self.window.blit(self.user_code_text, self.user_code_text_rect)
                        self.window.blit(self.user_code_currentLine, self.user_code_currentLine_rect)
                self.window.blit(self.exit, (912, 1))
                pygame.draw.rect(self.window, self.colors.down_bar, (0, 730, 950, 20))
                pygame.draw.rect(self.window, self.colors.left_bar, (0, 0, 45, 750))
                pygame.draw.rect(self.window, self.colors.grey, (0, 0, 1000, 25))
                self.window.blit(self.app_title, (400, 0))
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
                        # Create particles on click, if they are active (you can adjust the varis here)
                        if self.data.config["particles"]:
                            self.PartSYS.create_particles([self.data.mouse_pos[0], self.data.mouse_pos[1]], 12, 12)
                        if self.event.button == 1:
                            if self.exitbutton.collidepoint(self.data.mouse_pos):
                                # If the user wan't to exit, save his code and exit
                                with open("code.txt", "w+") as self.code:
                                    for line in range(self.user_code_lines):
                                        if line > 0:
                                            self.old_code = self.code.read()
                                            self.code.write(self.old_code + "\n{code}".format(code = self.user_code[line]))
                                        else:
                                            self.code.write("{code}".format(code = self.user_code[line]))
                                pygame.quit()
                                sys.exit()
                    elif self.event.type == KEYDOWN:
                        # If the pressed key is Backspace erase one space from the code
                        if self.event.key == K_BACKSPACE:
                            if self.currentState == "Editor":
                                if not self.user_code[self.user_code_lines - 1] == "":
                                    self.user_code[self.user_code_lines - 1] = self.user_code[self.user_code_lines - 1][0: - 1]
                                elif not self.user_code_lines == 1:
                                    self.user_code_lines -= 1
                        elif self.event.key == K_RETURN:
                            if self.currentState == "Editor":
                                self.user_code.append("")
                                self.user_code_lines += 1
                        # If the key is TAB make identation
                        elif self.event.key == K_TAB:
                            self.user_code[self.user_code_lines - 1] += "   "
                            if self.data.config["particles"]:
                                self.PartSYS.create_particles([self.user_code_text_rect.topright[0], self.user_code_text_rect.topright[1] + 10], 12, 12)
                        # If the key is not the above, add it as a string to the text
                        else:
                            if self.currentState == "Editor":
                                self.user_code[self.user_code_lines - 1] += self.event.unicode
                                if self.data.config["particles"]:
                                    self.PartSYS.create_particles([self.user_code_text_rect.topright[0], self.user_code_text_rect.topright[1] + 10], 12, 12)
                pygame.display.update()

        except Exception as error:
            self.currentState = "Error Screen"
            if self.RP.active:
                self.RP.update(large_image = "error", large_text = "Ran into an error", small_image = "appicon", small_text = "Pyncake Editor", state = "Ran into an error")
            self.ErrorScreen.draw(self.window, str(error))

if __name__ == "__main__":
    app()
