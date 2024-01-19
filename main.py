import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

COLORS = []

class balle:
    def __init__(self):
        self.x= 15
        self.y= 15
        self.changex= 1
        self.changey= 1
        self.rayon= 30


    def on_draw(self):
        arcade.draw_circle_filled(15, 30, 20, (255, 54, 34))


    def on_update(self):
        cercle_change_x = 3  # Nombre d'unité pour le déplacement sur l'axe des X
        cercle_change_y = 3  # Nombre d'unité pour le déplacement sur l'axe des Y
        self.x += self.changex
        self.y += self.changey
        if self.x < self.rayon:
            cercle_change_x *= -1
        if self.x > SCREEN_WIDTH - self.rayon:
            cercle_change_x *= -1
        if self.y < self.rayon:
            cercle_change_y *= -1
        if self.y > SCREEN_HEIGHT - self.rayon:
            cercle_change_y *= -1



class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Exercice #1")
        pass

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

    def on_mouse_press (self):
        balle()


def main():
    my_game = MyGame()
    my_game.setup()

    arcade.run()



main()
