import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Hello Pyxel",fps=30, quit_key=pyxel.KEY_Q, display_scale=10)
        pyxel.image(0).load(0, 0, "assets/pyxel_logo_38x16.png")
        pyxel.image(1).load(0, 0, "assets/noguchi_128x128.png")
        pyxel.image(2).set(
            0,
            0,
            [
                "10000000",
                "01000000",
                "00100000",
                "00010000",
                "00001000",
                "00000100",
                "00000010",
                "00000001",
            ],
        )
        pyxel.load("assets/sample.pyxres")
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
        #(x, y, image, )
        for i in range(3):
            x = 140 + i * 16
            y = 123 + pyxel.sin(pyxel.frame_count * 5.73 + i * 120.3) * 5
            col = 15 if pyxel.play_pos(i) else 13
            pyxel.pal(1, col)
            pyxel.blt(x, y, 2, 0, 0, 8, 8, 0)
        pyxel.pal()

        


App()
