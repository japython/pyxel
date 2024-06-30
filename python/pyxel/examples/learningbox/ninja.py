import pyxel
pyxel.init(128,128,title="NINJA")
pyxel.load("ninja.pyxres")

x = 8
#splite default x axis position
y = 35
#splite default y axis position

dx = 0

dy = 0

pldir = 1
#player direction status

chkpoint = [(2,0),(6,0),(2,7),(6,7)]

def chkwall(cx,cy):
    # To check whtether splite can move more
    # If can move, return 0, cannot , return more than 1

    c = 0

    if cx < 0 or pyxel.width -8 < cx:
        c = c + 1
        
    for cpx,cpy in chkpoint:
        xi = (cx + cpx)//8
        yi = (cy + cpy)//8
        if (1,0) == pyxel.tilemap(0).pget(xi,yi):
            c = c + 1
    return c

def update():
    global x,y,dx,dy,pldir

    if pyxel.btn(pyxel.KEY_LEFT):
        
        dx = -2
        pldir = -1

    elif pyxel.btn(pyxel.KEY_RIGHT):
        
        dx = 2
        pldir = 1
    
    else:

        dx = 0

    lr = pyxel.sgn(dx)
    loop = abs(dx)

    while 0 < loop :
        if chkwall( x + lr, y) != 0:
            dx = 0
            break

        x = x + lr
        loop = loop -1

    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    pyxel.blt(x, y, 0, 0, 8, pldir*8,8, 0)
    return

pyxel.run(update,draw)

