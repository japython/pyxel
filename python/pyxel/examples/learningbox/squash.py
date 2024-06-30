import pyxel
pyxel.init(256, 224, title="ball game", fps=30, capture_sec=60)

ball_x = 20
#ボール初期位置

ball_y = 30
#ボール初期位置

ball_r = 4
#ボールの半径

ball_dx = 6
#X軸の移動量

ball_dy = 4
#Y軸の移動量

bar_x = 20

bar_y = 204

bar_w = 40

bar_h = 4

def update():
    global ball_x,ball_y,ball_dx,ball_dy,bar_x

    ball_x += ball_dx
    #加算代入してどんどん位置更新

    if ball_x < 10 or pyxel.width - ball_r < ball_x :
        #ボール中心の座標位置が、円がX軸側にくっついた状態になるか、

        ball_dx = -ball_dx
        #移動を反転させるのにマイナスにする　よくよく見ると代入

    ball_y += ball_dy
    #X軸のボールの動きと同じ

    if ball_y < 10 or pyxel.height - ball_r < ball_y :
        ball_dy = -ball_dy
        #X軸のボールの動きと同じ

    if pyxel.btn(pyxel.KEY_RIGHT):
        if bar_x < 216:
            bar_x += 10

    elif pyxel.btn(pyxel.KEY_LEFT):
        if bar_x > 0 :
            bar_x -= 10

    if ( bar_x - 8 < ball_x < bar_x + bar_w + 16 ) and ( bar_y - 8 < ball_y < bar_y ) :
           ball_dy = -4 
           #- pyxel.rndi(0,2)

    return

def draw():
    pyxel.cls(0)

    pyxel.circ(ball_x, ball_y, ball_r, 10)

    pyxel.rect(bar_x, bar_y, bar_w, bar_h, 3)

    return

pyxel.run(update, draw)