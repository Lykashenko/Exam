from array import * 
d1 = []
for j in range(200):
    d2 = []
    for i in range(2):
        d2.append(0)
    d1.append(d2)

MoveRight = True
MoveLeft = True




class Sqr(object):
    def __init__(self, xpos, ypos, yspeed):
        self.c =0
        self.xpos = xpos
        self.ypos = ypos
        self.yspeed = yspeed

    def display (self):
        global MoveRight, MoveLeft
        rectMode(CENTER)
        fill(255, 200, 200)
        rect(self.xpos, self.ypos, 80, 80)
        line(self.xpos - 40, self.ypos, self.xpos + 40, self.ypos)
        line(self.xpos, self.ypos -40, self.xpos, self.ypos + 40)
        if self.yspeed == 0:
            x = self.xpos
            y = self.ypos
            for i in range(4):
                d1.remove([0, 0]) 
            d1.insert(0,[x - 20, y + 20]) 
            d1.insert(0,[x - 20, y - 20]) 
            d1.insert(0,[x + 20, y + 20]) 
            d1.insert(0,[x + 20, y - 20]) 
            self.xpos = 200
            self.ypos = 0  
            self.yspeed = 40
            MoveRight = True
            MoveLeft = True

    def drive (self):
        global MoveRight, MoveLeft
        if (frameCount % 10 == 0):
            self.ypos += self.yspeed 
        if self.ypos == 760:
            self.yspeed = 0
        if self.yspeed > 0 :
            if ((keyPressed) and (key == 'a') and self.xpos > 40 and MoveLeft == True):
                    self.xpos -= 40
                    MoveRight = True
                    MoveLeft = True
            if ((keyPressed) and (key == 'd') and self.xpos < 360 and MoveRight == True):
                    self.xpos += 40
                    MoveLeft = True
                    MoveRight = True
        if (frameCount % 10 != 0):
            if ((keyPressed) and (key == 's') and self.ypos < 760):
                self.ypos += 40
        for i in d1:
            if [self.xpos - 20, self.ypos + 60] == i:            
               self.yspeed = 0
            if [self.xpos + 20, self.ypos + 60] == i:            
               self.yspeed = 0
        for i in d1:
            if [self.xpos + 60, self.ypos + 20] == i:
                MoveRight = False
            if [self.xpos + 60, self.ypos - 20] == i:
                MoveRight = False
        for i in d1:
            if [self.xpos - 60, self.ypos + 20] == i:
                MoveLeft = False
            if [self.xpos - 60, self.ypos - 20] == i:
                MoveLeft = False

                
   

        
          
                
    
            
        
           

    





block1=Sqr(200, 0, 40)

def setup():
    size(400, 800)
    frameRate(30)
    
def draw():
    background(0)
    for i in range(9):
        line(40 + i*40, 0, 40 + i*40, 800)
        stroke(78) 
    for i in range(19):
        line(0, 40 + 40*i, 400, 40 + 40 *i)
    block1.display()
    block1.drive()
    for n in range(0, 199):
            e = d1[n][0]
            b = d1[n][1]
            if e != 0:
                rect(e, b, 40, 40)




        
