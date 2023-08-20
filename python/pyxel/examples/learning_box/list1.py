import pyxel

pyxel.init(128,128)
pyxel.load("assets/sample.pyxres")

width=8
height=8

#split_A = 8,0
#split_B = 16,0

x=0
y=0
status=0

def update():
    global x,y,status
    #if no status here, text in def draw doesn't show

    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    #x = pyxel.mouse_x
    #y = pyxel.mouse_y

    if x == 5 and y ==5:
        status = 1
    else:
        status = 0

    return
    

def draw():
    pyxel.cls(10)
    pyxel.rect(5,5,30,30,2)
    pyxel.rect(30,30,15,50,11)
    pyxel.blt(50,50,0,8,0,8,8,0)
    pyxel.blt(70,70,0,16,0,8,8,0)

    if status==1:
        pyxel.text(20,7,'Hello World!',7)

    return

pyxel.run(update,draw)