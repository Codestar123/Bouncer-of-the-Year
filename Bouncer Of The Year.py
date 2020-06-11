from tkinter import *
import random
import time
import winsound
class Ball:
    def __init__(self,canvas):
        self.canvas_b = canvas
        self.color_opt_b = ['red','green','blue','orange','purple','violet','magenta']
        self.color_b = random.choice(self.color_opt_b)
        self.oval = self.canvas_b.create_oval(10, 10, 25, 25, fill = self.color_b,
outline = self.color_b)
        self.canvas_b.move(self.oval, 237, 140)
        self.wid_opt_b = [1,2,3,-3,-2,-1]
        random.shuffle(self.wid_opt_b)
        self.wid_pos_b = self.wid_opt_b[1]
        self.hei_pos_b = -3
        self.canvas_height_b = self.canvas_b.winfo_height()
        self.pos_b = []
        self.canvas_width_b = self.canvas_b.winfo_width()
        self.hit_bot = False
        self.point = 0
    def touched_the_paddle (self):
        paddle_pos = self.canvas_b.coords(paddle.rectangle)
        if self.pos_b[0] <= paddle_pos[2] and self.pos_b[2] >= paddle_pos[0]:
            if self.pos_b[3] >= paddle_pos[1] and self.pos_b[3] < paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas_b.move(self.oval, self.wid_pos_b, self.hei_pos_b)
        self.pos_b = self.canvas_b.coords(self.oval)
        if self.pos_b[1] <= 0:
            self.hei_pos_b = 1

        if self.pos_b[3] >= self.canvas_height_b:
            self.hei_pos_b = -1

        if self.pos_b[0] <= 0:
            self.wid_pos_b = 3

        if self.pos_b[2] >= self.canvas_width_b:
            self.wid_pos_b = -3

        if self.touched_the_paddle() == True:
            self.hei_pos_b = -3
            winsound.Beep(1100,25)

        if self.pos_b[3] >= self.canvas_height_b:
            self.hit_bot = True
            time.sleep(0.1)
            self.canvas_b.create_text(250,200,text = 'Game Over',fill = 'black',
            font = ('Times',50))



class Paddle:
    def __init__(self,canvas):
        self.canvas_p = canvas
        self.color_opt_p = ['red','green','blue','orange','purple','violet','magenta']
        self.color_p = random.choice(self.color_opt_p)
        self.rectangle = canvas.create_rectangle(0,0,100,10,fill = self.color_p,
outline = self.color_p)
        self.canvas_p.move(self.rectangle,200,300)
        self.wid_p = 0
        self.canvas_width_p = self.canvas_p.winfo_width()
        self.pos_p = []
        self.canvas_p.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas_p.bind_all('<KeyPress-Right>',self.turn_right)

    def draw (self):
        self.canvas_p.move(self.rectangle,self.wid_p,0)
        self.pos_p = self.canvas_p.coords(self.rectangle)
        if self.pos_p[0] <= 0:
            self.wid_p = 2
        elif self.pos_p[2] >= self.canvas_width_p:
            self.wid_p = -2
    def turn_left (self,evt):
        self.wid_p = -2
    def turn_right (self,evt):
        self.wid_p = 2


class Control:
    def __init__ (self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<Button-1>', self.start)
        self.can_start = False
    def start (self, event):
        self.can_start = True

class Points:
    def __init__(self,canvas):
        self.canvas = canvas
        self.hei = self.canvas.winfo_height()
        self.points = 0
        self.point = self.canvas.create_text(250, 10, text=0, fill='black',
font=('Times', 20))
    def count_points (self):
        if ball.touched_the_paddle() == True:
            self.points = self.points + 1
            self.canvas.itemconfig(self.point,text = self.points,fill = 'black')




tk = Tk()
tk.title('Bouncer Of The Year')
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk,width = 500,height = 400,bd = 0,highlightthickness = 0)
canvas.pack()
tk.update()

ball = Ball(canvas)
paddle = Paddle(canvas)
control = Control(canvas)
points = Points(canvas)
while 1:
    if control.can_start == True:
        if ball.hit_bot == False:
            ball.draw()
            paddle.draw()
            points.count_points()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
