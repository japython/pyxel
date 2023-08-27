import pyxel

pyxel.init(100,100)

def update():
    count = pyxel.frame_count

def draw():
    pyxel.text(10,10, count)


pyxel.run(update, draw)