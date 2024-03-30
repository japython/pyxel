import pyxel
pyxel.init(128,128,title="NINJA")
pyxel.load("ninja.pyxres")

x = 8
#splite default position
y = 85
#splite default position

pldir = 1
# What are those variable above? > player direction 

def update():
    global x,y,dx,dy,pldir
    # to use variable came from outside of funstion, global setting necesarry


    if pyxel.btn(pyxel.KEY_LEFT):
        
        #dx = -2
        x -= 2
        pldir = -1


    elif pyxel.btn(pyxel.KEY_RIGHT):
        
        #dx = 2
        x += 2
        pldir = 1

    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    pyxel.blt(x, y, 0,  0, 8, pldir*8,8, 0)
    return

pyxel.run(update,draw)

