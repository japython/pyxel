import pyxel
pyxel.init(128,128,title="NINJA")
pyxel.load("ninja.pyxres")

x = 8
#splite default x axis position
y = 100
#splite default y axis position

dx = 0

dy = 0

pldir = 1
#player direction status

<<<<<<< HEAD
#chkpoint = [(0,0),(8,0),(0,8),(8,8)]
=======
chkpoint = [(2,0),(6,0),(2,7),(6,7)]
>>>>>>> aca81296fa8bc831c502be4ae878c9e1ebbb255f

#def chkwall(cx,cy):
    #c = 0
    #if cx < 0 or pyxel.width -8 < cx:
    #    c = c + 1
    #for cpx,cpy in chkpoint:
    #    xi = (cx + cpx)//8
     #   yi = (cy + cpy)//8
     #   if (1,0) == pyxel.tilemap(0).pget(xi,yi):
     #       c = c + 1
    #return c

def update():
    global x,y,dx,dy,pldir
    # to use variable came from outside of funstion, global setting necessarry

    if pyxel.btn(pyxel.KEY_LEFT):
        
        dx = -2
        pldir = -1


    elif pyxel.btn(pyxel.KEY_RIGHT):
        
        dx = 2
        pldir = 1
    
    else:

        dx = 0
    
    x += dx
    # I cannot understand why dx and dy are necessary besides x and y though, it is easier to maintain and controle movement with flexibility.

    
<<<<<<< HEAD
    #lr = pyxel.sgn(dx)
    
    #loop = abs(dx)
    #while 0 < loop :
        #if chkwall( x + lr, y) != 0:
        #    dx = 0
        #    break
        #x = x + lr
        #loop = loop -1
=======
    lr = pyxel.sgn(dx)
    #Returns 1 when x is positive, 0 when it is zero, and -1 when it is negative
    loop = abs(dx)
    #
    while 0 < loop :
        if chkwall( x + lr, y) != 0:
            dx = 0
            break
        x = x + lr
        loop = loop -1
>>>>>>> aca81296fa8bc831c502be4ae878c9e1ebbb255f
    
    return

    

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    pyxel.blt(x, y, 0, 0, 8, pldir*8,8, 0)
    return

pyxel.run(update,draw)

