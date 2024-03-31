import pyxel

class App:
    def __init__(self):
        pyxel.init(128, 128, title="Hello Pyxel",fps=30, quit_key=pyxel.KEY_Q, display_scale=10)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/noguchi_128x128.png")
        pyxel.load("assets/sample_test.pyxres")
        #pyxel.image(0).set(50, 50, ["0123", "4567", "89ab", "cdef"])
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        #if pyxel.btnp(pyxel.KEY_Q):
            #pyxel.quit()
        
        pass
        

    def draw(self):
        pyxel.cls(1)
        pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
        pyxel.text(55, 50, str(pyxel.frame_count), 3)
        #テキスト選択の値を入れるだけで認識される（col= はなくてもOK）

        pyxel.text(55, 60, 'Good Bye !', col=10)
        #pyxel.text(55, 20, str(pyxel.mouse_x), 10)
        #pyxel.text(65, 20, str(pyxel.mouse_y), 10)
        pyxel.blt(70, 70, 0, 0, 0, 38, 16)
        pyxel.blt(70, 90, 1, 0, 8, 16, 8)
        pyxel.bltm(0, 0, 0, 0, 0, 128, 128)
        #(x, y, image, )

        
App()
