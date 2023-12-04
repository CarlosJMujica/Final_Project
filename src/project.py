import pygame
from tkinter import filedialog, Tk


class Mpen():
    def __init__(self):
        self.bcolor = pygame.Color(255, 0, 0)
        self.drawing = False

    def draw(self, screen, x, y):
        if self.drawing:
            pygame.draw.rect(screen, self.bcolor, (x, y, 5, 5))


class BackgroundColor():
    def __init__(self, color):
        self.color = pygame.Color(color)



def main():
    pygame.init()
    pygame.display.set_caption("Art Board")
    clock = pygame.time.Clock()

    resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    running = True

    pen = Mpen()
    bg_color = BackgroundColor((255,255,255))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pen.bcolor = pygame.Color(255, 0, 0)
                elif event.key == pygame.K_2:
                    pen.bcolor = pygame.Color(0, 255, 0)
                elif event.key == pygame.K_3:
                    pen.bcolor = pygame.Color(0, 0, 255)
                elif event.key == pygame.K_4:
                    pen.bcolor = pygame.Color(255, 255, 0)
                elif event.key == pygame.K_5:
                    pen.bcolor = pygame.Color(0, 255, 255)
                elif event.key == pygame.K_6:
                    pen.bcolor = pygame.Color(255, 0, 255)
                elif event.key == pygame.K_e:
                    pen.bcolor = bg_color.color
                elif event.key == pygame.K_q:
                    pen.bcolor = pygame.Color(0, 0, 0)
                elif event.key == pygame.K_r:
                    screen.fill(pygame.Color(255,0,0))
                elif event.key == pygame.K_g:
                    screen.fill(pygame.Color(0,255,0))
                elif event.key == pygame.K_b:
                    screen.fill(pygame.Color(0,0,255))
                elif event.key == pygame.K_d:
                    screen.fill(pygame.Color(255,255,255))
                elif event.key == pygame.K_a:
                    screen.fill(pygame.Color(0,0,0))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pen.drawing = True
            elif event.type == pygame.MOUSEBUTTONUP:
                pen.drawing = False

        px, py = pygame.mouse.get_pos()
        pen.draw(screen, px, py)

        pygame.display.update()
        clock.tick(90000)

    Tk().withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        pygame.image.save(screen, file_path)
    pygame.quit()



if __name__ == "__main__":
    main()