import pyxel
pyxel.init(128,128,title="maze_dev")
pyxel.load("assets\maze.pyxres")

x = 8   #初期位置
y = 112 #初期位置
dx = 0
dy = 0
pldir = 1 #方向変換した場合のスプライトの向きを変える値

chkpoint = [(2,0),(6,0),(2,7),(6,7)]

def chkwall(cx,cy):
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

    # 操作判定
    if pyxel.btn(pyxel.KEY_LEFT):
        dx = -2
        pldir = -1
    elif pyxel.btn(pyxel.KEY_RIGHT):
        dx = 2
        pldir = 1
    else:
        dx = 0

    if pyxel.btn(pyxel.KEY_UP):
        dy = -2
    elif pyxel.btn(pyxel.KEY_DOWN):
        dy = 2  
    else:
        dy = 0
    

    # 横方向の移動

    lr = pyxel.sgn(dx)
    loop = abs(dx)
    while 0 < loop :
        if chkwall( x + lr, y) != 0:
            dx = 0
            break
        x = x + lr
        loop = loop -1
    
       # 縦方向の移動
    ud = pyxel.sgn(dy)
    loop = abs(dy)
    while 0 < loop:
        if chkwall(x, y + ud) != 0:
            dy = 0
            break
        y = y + ud
        loop = loop - 1
    
    return

def draw():
    pyxel.cls(0)
    pyxel.bltm(0,0, 0, 0,0, pyxel.width,pyxel.height, 0)
    pyxel.blt( x, y, 0,  0, 8, pldir*8,8, 0)
    return

pyxel.run(update,draw)