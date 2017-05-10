
from tkinter import *
import random
import time

class Ball:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color) #공 좌표 및 색깔(oval : object 형태 타입)
                               #        ↑   ↑  ↑    ↑
      #좌측상단  구석에서 시작하는  x  y   우측 상단 구석에서 시작하는 x y

        self.canvas.move(self.id, 245, 100) #공을 캔버스 중앙으로 이동

    def draw(self):
        pass


tk = Tk()     # 1. tk 를 인스턴스화 한다.
tk.title("Game")  # 2. tk 객체의 title 메소드(함수)로 게임창에 제목을 부여한다.
tk.resizable(0, 0) # 3. 게임창의 크기는 가로나 세로로 변경될수 없다라고 말하는것이다.
tk.wm_attributes("-topmost", 1) #4. 다른 모든 창들 앞에 캔버스를 가진 창이 위치할것을 tkinter 에게 알려준다.
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
     # bg=0,highlightthickness=0 은 캔버스 외곽에 둘러싼
     # 외곽선이 없도록 하는것이다. (게임화면이 좀더 좋게)
canvas.pack()       # 앞의 코드에서 전달된 폭과 높이는 매개변수에 따라 크기를 맞추라고 캔버스에에 말해준다.
tk.update()   # tkinter 에게 게임에서의 애니메이션을 위해 자신을 초기화하라고 알려주는것이다.

ball = Ball(canvas,'red')

while 1:
    tk.update_idletasks()   # 우리가 창을 닫으라고 할때까지 계속해서 tkinter 에게 화면을 그리고 
    tk.update() 
    time.sleep(0.01)  # 100분의 1초마다 잠들어라 ! 