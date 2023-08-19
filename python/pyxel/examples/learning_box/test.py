import pyxel

pyxel.init(100,100)
pyxel.load("test.pyxres")

splite_width=8
splite_height=8

x=0
y=0
status=0 #変数追加

def update():
    global x,y, status
    x = pyxel.mouse_x
    y = pyxel.mouse_y
    if x==10 and y==10:
        status=1
    else:
        status=0

    return

def draw():
    pyxel.cls(1)
    pyxel.blt(x,y,0,16,40,splite_width,splite_height,0)
    pyxel.blt(10,10,0,64,16,splite_width,splite_height,11)

    if status==1:
        pyxel.text(20,7,'Hello world!',7)

    return

pyxel.run(update,draw)