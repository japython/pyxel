import pyxel

pyxel.init(256, 256, title="Pygame")
pyxel.load("mygame.pyxres")

x = 0
y = 0 

def update():
    global x, y
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    return

def draw():

    pyxel.cls(1)
    pyxel.rect(5, 5, 16, 16, 13)

    pyxel.blt(x, y, 0, 0, 0, 16, 16, 11)
    return



pyxel.run(update, draw)