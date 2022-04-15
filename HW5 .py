"""
Authors :Mohan Thapa 
        :Gaurab Sapkota 
"""


from tkinter import *
from tkinter.messagebox import *

class Ball (Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Pong Game")
        self.grid()
        canvas_width = 800
        canvas_height =400
        self.canvas = Canvas(self,width = canvas_width, height = canvas_height , bg = "white")
        self.canvas.grid (row = 1)

        # setting the number of lives 
        self.lives = 5

        # drawing the ball 
        diameter = 20
        top_x = 2
        top_y = 2 
        ball = self.canvas.create_oval(top_x, top_y, top_x + diameter, top_y + diameter , fill = "red", tags = "ball" )

        horizontal_direction = "east"
        vertical_direction = "south "

        dx = 5
        dy = 5

        #drawing rectangle

        self.paddleTopx = 360
        self.paddleTopy = 380
        self.paddlewidth = 80
        self.paddleheight = 20

        self.paddle = self.canvas.create_rectangle(self.paddleTopx, self.paddleTopy, self.paddleTopx+ self.paddlewidth,self.paddleTopy+ self.paddleheight, fill = "black", tags = "rect")


        # drawing moving paddle
        self.canvas.focus_set()
        self.canvas.bind('<KeyPress-Left>', self.moveLeft)
        self.canvas.bind('<KeyPress-Right>', self.moveRight)


        while True:
            try:
                if horizontal_direction == "east":
                    top_x += dx
                    if top_x >= (canvas_width - diameter):
                        horizontal_direction = "west"
                    self.canvas.move("ball", dx, 0)

                else:
                    top_x -= dx 
                    if top_x <= 0:
                        horizontal_direction = "east"
                    self.canvas.move("ball", -dx, 0)  

                if vertical_direction == "south":
                    top_y += dy
                    if top_y >= (canvas_height - diameter):
                        vertical_direction = "north"
                    self.canvas.move("ball", 0, dy)


                    if top_y >= 350:
                        leftPaddle = self.paddleTopx <= top_x <=(self.paddleTopx +80)
                        rightPaddle = self.paddleTopx <= top_x+80 <=(self.paddleTopx +80)
                        if leftPaddle or rightPaddle:
                            vertical_direction = "north"
                            self.canvas.move("ball", 0, dy)


                    if top_y >= 380:
                        self.lives -= 1

                else:
                    top_y -= dy
                    if top_y <= 0:
                        vertical_direction = "south"
                    self.canvas.move("ball", 0, -dy)
            except:
                break

            self._label = Label(self, text = "Lives Left: " + str(self.lives), font =("Verdana", 20))
            self._label.grid(row = 0)

            if self.lives == 0:
                
                self.canvas.delete ("ball")
                ball = self.canvas.create_oval(2, 2, 2 + diameter, 2 + diameter, fill = "red" , tags = "ball")
                self.destroy()
                self.__init__()
                break


            self.canvas.after(15)
            self.canvas.update()


    def moveLeft (self, event):
        if self.paddleTopx >= 5:
            self.canvas.delete ("rect")
            self.paddleTopx -= 5
        self.canvas.create_rectangle (self.paddleTopx, self.paddleTopy, self.paddleTopx+ self.paddlewidth,self.paddleTopy+ self.paddleheight, fill = "black", tags = "rect")

  

    def moveRight (self, event):
        if self.paddleTopx <= 720:
            self.canvas.delete ("rect")
            self.paddleTopx += 5
            self.canvas.create_rectangle (self.paddleTopx, self.paddleTopy, self.paddleTopx+ self.paddlewidth,self.paddleTopy+ self.paddleheight, fill = "black", tags = "rect")

def main(): 
    Ball().mainloop()
main()