import arcade
import random

SW = 640
SH = 480
speed = 3
bullet_speed = 6

#INSTRUCTIONS
#WASD/ARROW KEYS TO MOVE
#L/R SHIFT TO SHOOT


class Guy(arcade.Sprite):
    def __init__(self, colorvar):
        super().__init__()
        self.textures = []
        self.test = arcade.load_texture(f"{colorvar}.png")
        self.textures.append(self.test)
        self.shoot = arcade.load_texture(f"{colorvar}shoot.png")
        self.textures.append(self.shoot)
        self.fliptest = arcade.load_texture(f"{colorvar}.png", flipped_horizontally=True)
        self.textures.append(self.fliptest)
        self.flipshoot = arcade.load_texture(f"{colorvar}shoot.png", flipped_horizontally=True)
        self.textures.append(self.flipshoot)
        self.texture = self.textures[0]
        self.shoot_sound = arcade.load_sound("sounds/mp3s/shoot.mp3")
        self.death_sound = arcade.load_sound("sounds/mp3s/death.mp3")
        self.victory_sound = arcade.load_sound("sounds/mp3s/victory.mp3")
        self.dx = 0
        self.dy = 0
        self.shooting = False
        self.l = False

    def update_guy(self):

        if self.center_x < 0:
            self.center_x = SW
        if self.center_x > SW:
            self.center_x = 0

        if self.center_y < 0:
            self.center_y = SH
        if self.center_y > SH:
            self.center_y = 0

        self.center_x += self.dx
        self.center_y += self.dy

        if self.shooting:
            if self.l:
                self.texture = self.textures[3]
            else:
                self.texture = self.textures[1]
        if not self.shooting:
            if not self.l:
                self.texture = self.textures[0]
            else:
                self.texture = self.textures[2]


class Bullet:
    def __init__(self):
        ""


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color_from_hex_string("ffdcdc"))
        self.redguy = Guy("r")
        self.blueguy = Guy("b")
        self.redguy.center_x = random.randint(1+40, SW-40)
        self.redguy.center_y = random.randint(1+40, SH-40)
        self.blueguy.center_x = random.randint(1+40, SW-40)
        self.blueguy.center_y = random.randint(1+40, SH-40)

    def on_draw(self):
        arcade.start_render()
        self.redguy.draw()
        self.blueguy.draw()

    def on_update(self, dt):
        self.redguy.update_guy()
        self.blueguy.update_guy()

    def on_key_press(self, key, modifiers):
        #movement
        if key == arcade.key.LEFT:
            self.redguy.dx = -speed
            self.redguy.l = True
        elif key == arcade.key.RIGHT:
            self.redguy.dx = speed
            self.redguy.l = False
        elif key == arcade.key.UP:
            self.redguy.dy = speed
        elif key == arcade.key.DOWN:
            self.redguy.dy = -speed
        if key == arcade.key.A:
            self.blueguy.dx = -speed
            self.blueguy.l = True
        elif key == arcade.key.D:
            self.blueguy.dx = speed
            self.blueguy.l = False
        elif key == arcade.key.W:
            self.blueguy.dy = speed
        elif key == arcade.key.S:
            self.blueguy.dy = -speed

        #shooting
        if key == arcade.key.LSHIFT:
            if not self.blueguy.shooting:
                self.blueguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 0.25)
            else:
                self.blueguy.shooting = False

        if key == arcade.key.RSHIFT:
            if not self.redguy.shooting:
                self.redguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 0.25)
            else:
                self.redguy.shooting = False

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.redguy.dx = 0
            self.redguy.l = True

        if key == arcade.key.RIGHT:
            self.redguy.dx = 0
            self.redguy.l = False

        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.redguy.dy = 0

        if key == arcade.key.A:
            self.blueguy.l = True
            self.blueguy.dx = 0

        if key == arcade.key.D:
            self.blueguy.dx = 0
            self.blueguy.l = False

        elif key == arcade.key.W or key == arcade.key.S:
            self.blueguy.dy = 0

        if key == arcade.key.LSHIFT:
            if not self.blueguy.shooting:
                self.blueguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 5)
            else:
                self.blueguy.shooting = False

        if key == arcade.key.RSHIFT:
            if not self.redguy.shooting:
                self.redguy.shooting = True
                arcade.play_sound(self.redguy.shoot_sound, 5)
            else:
                self.redguy.shooting = False


def main():
    MyGame(SW, SH, "TRIPLE A FPS GAME")
    arcade.run()


if __name__ == "__main__":
    main()