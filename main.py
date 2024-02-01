import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = [arcade.color.RED, arcade.color.GREEN, arcade.color.BLUE,  arcade.color.ORANGE]

class balle:
    def __init__(self, x, y):
        self.x= x
        self.y= y
        self.changex= 300
        self.changey= 300
        self.rayon= random.randint(10, 30)
        self.color = random.choice(COLORS)

    # dessiner la balle à l’écran
    def on_draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)

    # mise à jour de la position de la balle
    def on_update(self):

        self.x += self.changex
        self.y += self.changey
        if self.x < self.rayon:
            self.changex *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            self.changex *= -1
        if self.y < self.rayon:
            self.changey *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            self.changey *= -1

class rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.changex = 300
        self.changey = 300
        self.color = random.choice(COLORS)
        self.height = random.randint(20,30)
        self.width = random.randint(20, 30)
        self.tilt_angle = random.randint(0, 90)

        # dessiner le rectangle à l’écran
    def on_draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.height, self.width, self.color, self.tilt_angle)

    # mise à jour du rectangle
    def on_update(self):

        self.x += self.changex
        self.y += self.changey
        if self.x < self.height:
            self.changex *= -1
        if self.x > SCREEN_WIDTH - self.height:
            self.changex *= -1
        if self.y < self.width:
            self.changey *= -1
        if self.y > SCREEN_HEIGHT - self.width:
            self.changey *= -1



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        self.liste_balles = []
        self.liste_rectangle = []

    def setup(self):
        pass

#desiner le rectangle et les balles dans les listes
    def on_draw(self):
        arcade.start_render()
        for i in self.liste_balles:
            i.on_draw()
        for j in self.liste_rectangle:
            j.on_draw()

#dessiner une balle ou un rectangle a l'endroit du clic
    def on_mouse_press (self,x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            nouvelle_balle = balle(x,y)
            self.liste_balles.append(nouvelle_balle)
        if button == arcade.MOUSE_BUTTON_RIGHT:
            nouveau_rectangle = rectangle(x,y)
            self.liste_rectangle.append(nouveau_rectangle)

    # fait le programme (update)
    def on_update(self, delta_time: float):
        for i in self.liste_balles:
            i.on_update()

        for j in self.liste_rectangle:
            j.on_update()

#tous le jeu
def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()



main()
