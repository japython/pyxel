import pyxel
import random

pyxel.init(80,64,title="rock paper scissors")
pyxel.load("janken.pyxres")
pyxel.mouse(True)

com_hand=0

status =0 

def update():
    
    global com_hand, status

    if status == 0:

        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            com_hand = random.randint(0,2)

            status = 1

        else:
            com_hand = int(pyxel.frame_count / 5) % 3
    
    elif status == 1:
        pass

    return

def draw():
    pyxel.cls(0)

    # コンピューターの手を描画
    pyxel.text(4,10, "COM",7)
    pyxel.blt(32,10, 0, com_hand*16,0, 16,16, 0)

    # プレーヤーの手を描画
    pyxel.text(4,32, "YOU",7)
    pyxel.blt(16,32, 0,  0,0, 16,16, 0)
    pyxel.blt(32,32, 0, 16,0, 16,16, 0)
    pyxel.blt(48,32, 0, 32,0, 16,16, 0)
    
    return

pyxel.run(update, draw)