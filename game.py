#!/usr/bin/env python3

import pyxel


class App:
    def __init__(self):
        pyxel.init(160, 120, caption="test lol")
        pyxel.load("assets/data.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "test lol", 15)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)


if __name__ == "__main__":
    App()
