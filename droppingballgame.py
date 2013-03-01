##   Bombs n' Balls   ##
##  By Matt Perrelli  ##
########################

from graphics import *
import random
import time
import os

#depending on OS change text size
textsizechange = 0
if os.name == "posix":
    textsizechange = 0
if os.name == "nt":
    textsizechange = 4
else:
    textsizechange = 0

titlewin = GraphWin ("Bombs n' Balls", 600, 600)
title = Image(Point(300,300), "bombsnballstitlescreen.gif")
title.draw(titlewin)
titlewin.getMouse()
titlewin.close()
while True:
    win = GraphWin ("Bombs n' Balls", 600, 600, autoflush=False)

    balls = []
    detstars = []
    detonators = []
    clickdets = []
    clickdetbomb = []

    #Draw text verticly
    def VertText(x, y, string, color, spacing, Hoffset, size):
        tempstring = string
        for i in range(len(tempstring)):
            my = spacing * i
            mx = Hoffset * i
            char = Text(Point(x + mx, y + my), tempstring[i])
            char.setSize(size - textsizechange)
            char.setFill(color)
            char.draw(win)

    #Draw Rectangle function
    def DrawBlocks(x1, y1, x2, y2, fill, window):
        block = Rectangle(Point(x1, y1), Point(x2, y2))
        block.setFill(fill)
        block.draw(window)

    #Draw text function
    def DrawText(x, y, string, color, size, window):
        word = Text(Point(x, y), string)
        word.setSize(size - textsizechange)
        word.setFill(color)
        word.draw(window)

    #Pause function
    def paused():
        pausewin = GraphWin ("Paused!!", 200, 100, autoflush=False)
        bg = Image(Point(100,50), "balldropgamebg_pause.gif")
        bg.draw(pausewin)
        try:
            pausewin.getMouse()
            pausewin.close()
        except:
            pass

    #About function
    def about():
        aboutwin = GraphWin ("About", 300, 500, autoflush=False)
        bg = Image(Point(150,250), "balldropgamebg_about.gif")
        bg.draw(aboutwin)
        DrawText(100, 25, "Instructions and stuff", "black", 20, aboutwin)
        detbomb = Image(Point(30, 130), "balldropgame_bomb.gif")
        detbomb.draw(aboutwin)
        DrawText(180, 130, "Bombs are attained by clicking the\n small red balls that fly Horizontally\n across your screen.", "black", 14, aboutwin)
        detstara = Circle(Point(30, 210) , 10)
        detstara.setFill("red")
        detstara.draw(aboutwin)
        DrawText(180, 210, "Click these to get Bombs!\n These are also worth 15 points.", "black", 14, aboutwin)
        circ = Circle(Point(40, 290), 30)
        circ.setFill(random.choice(["green", "red", "blue", "orange"]))
        circ.draw(aboutwin)
        DrawText(180, 290, "Click these balls before they\n reach the spikes! They are \nworth 8 points each.", "black", 14, aboutwin)
        DrawText(150, 370, "Dont get spiked!", "black", 22, aboutwin)
        DrawText(150, 425, "A game by Matt Perrelli\n mperrelli.com", "black", 15, aboutwin)
        try:
            aboutwin.getMouse()
            aboutwin.close()
        except:
            pass

    #Stall function
    def stall():
        time.sleep(2)

    #Draw detonator function
    def detonator():
        y = 198
        for i in range(len(clickdets)):
            y += 50
        det = Circle(Point(26, y), 23)
        det.setFill("red")
        det.draw(win)
        detbomb = Image(Point(26, y), "balldropgame_bomb.gif")
        detbomb.draw(win)
        clickdets.append(det)
        clickdetbomb.append(detbomb)

    #Draw background and pause/about buttons
    bg = Image(Point(300,300), "balldropgamebg2.gif")
    bg.draw(win)
    VertText(10, 87, "Pause", "black", 13, 3, 16)
    VertText(10, 14, "About", "black", 11, 3, 14)

    #Point counter
    points = 0
    txtpoints = Text(Point(540, 15), points)
    txtpoints.setSize(16)
    txtpoints.draw(win)

    #Initial variables
    timecheck=0
    dx = 0
    dy = 2
    interval=30
    lost = False
    
    #Save score and call up high score list.
    def HighScores():
        en = Entry(Point(300,200), 10)
        en.draw(win)
        en.setText("Name")
        point = str(points)
        btn = Rectangle(Point(200,220), Point(298,250))
        btn2 = Rectangle(Point(302, 220), Point(400,250))
        scores = "------------------------\n"
        scores2 = "------------------------\n"
        hs = Text(Point(225, 400), scores)
        hs.setSize(14 - textsizechange)
        hs.draw(win)
        hs2 = Text(Point(375, 400), scores)
        hs2.setSize(14 - textsizechange)
        hs2.draw(win)
        file3 = open("scores.dat", "r")
        #High scores
        disordered = []
        for line in file3:
            s = line.split('-', 1)
            score = int(s[1])
            disordered.append( (score, line) )
        disordered.sort()
        disordered.reverse()
        lines = []
        for s in disordered:
            lines.append(s[1])
        if len(lines) < 10:
            numrange = len(lines)
        else:
            numrange = 6
        for i in range(numrange):
            scores = scores + lines[i] + "------------------------\n"
        hs.setText(scores)
        file3.close()
        file4 = open("scores.dat", "r")
        #Recent scores
        lines2 = []
        for line in file4:
            lines2.append(line)
        lines2.reverse()
        if len(lines2) < 10:
            numrange2 = len(lines2)
        else:
            numrange2 = 6
        for i in range(numrange2):
            scores2 = scores2 + lines2[i] + "------------------------\n"
        hs2.setText(scores2)  
        btn2.draw(win)
        btn.draw(win)
        btnt = Text(Point(249,237), "Submit Score!")
        btnt2 = Text(Point(350,237), "Play Again")
        moartext = Text(Point(225,280), "High Scores!")
        moartext.setSize(14 - textsizechange)
        moartext.draw(win)
        moartext2 = Text(Point(375,280), "Recent Scores...")
        moartext2.setSize(14 - textsizechange)
        moartext2.draw(win)
        btnt2.draw(win)
        btnt.draw(win)
        click = False
        while click == False:
            p = win.getMouse()
            y = p.getY()
            x = p.getX()
            if x < 298 and x > 200 and y < 250 and y > 220:
                en.undraw()
                btn.undraw()
                btnt.undraw()
                moartext.undraw()
                moartext2.undraw()
                hs2.undraw()
                t.undraw()
                btn2.undraw()
                btnt2.undraw()
                btnt = Text(Point(300,100), "High Scores!")
                btnt.setSize(20 - textsizechange)
                btnt.draw(win)
                scores2 = "------------------------\n"
                #Write info to scores.dat
                name = str(en.getText())
                writestr = str(name + " - " + point + "\n")
                file1 = open("scores.dat", "r+")
                writeexist = str(file1.readlines())
                file1.write(writestr)
                file1.close()
                #Display new list of scores
                file = open("scores.dat", "r+")
                disordered2 = []
                for line in file:
                    s = line.split('-', 1)
                    score = int(s[1])
                    disordered2.append( (score, line) )
                disordered2.sort()
                disordered2.reverse()
                lines = []
                for s in disordered2:
                    lines.append(s[1])
                if len(lines) < 10:
                    numrange2 = len(lines)
                else:
                    numrange2 = 10
                for i in range(numrange2):
                    scores2 = scores2 + lines[i] + "------------------------\n"
                hs.move(75,-100)
                hs.setText(scores2)
                win.update()
                win.getMouse()
                break
            if x < 400 and x > 302 and y < 250 and y > 220:
                break

    #Game loop
    while lost != True:
        #Increasing difficulty control
        if timecheck % 200 == 0:
            dy += 2
            interval -= 2
            
        #Draw the balls
        if timecheck % interval == 0:
            c = Circle(Point(random.randint(60, 570),-40), random.randint(20,40))
            c.setFill(random.choice(["green", "red", "blue", "orange"]))
            c.draw(win)
            balls.append(c)
            
        #Draw detonator
        if timecheck > 100:
            if timecheck % 400 == 0:
                detstar = Circle(Point(0, random.randint(50, 500)), 10)
                detstar.setFill("red")
                detstar.draw(win)
                detstars.append(detstar)
        for i in range (len(detstars)):
            detstars[i].move(15,0)
            if detstars[i].getCenter().getX() > 610:
                detstars[i].undraw()
                del detstars[i]
                
        #Move the balls
        for i in range (len(balls)):
            balls[i].move(dx,dy)
            #Test if any of the balls hit the spikes
            if balls[i].getCenter().getY() > 550:
                lost=True
                
        #Look for mouse clicks
        p = win.checkMouse()
        if p != None:
            y = p.getY()
            x = p.getX()

            #Check balls
            todel = []
            for i in range(len(balls)):
                #Check if clicks are within a ball
                #If yes, delete ball and update points
                if ((x - (balls[i].getCenter().getX()))**2 + (y - (balls[i].getCenter().getY()))**2) <= (balls[i].getRadius()**2):
                    points += 9
                    balls[i].undraw()
                    todel.append(balls[i])
            for ball in todel:
                balls.remove(ball)
                
            #Check detonators 
            for i in range(len(detstars)):
                #Check if clicks are within a detonator
                #If yes, add detonator to list available to use
                if ((x - (detstars[i].getCenter().getX()))**2 + (y - (detstars[i].getCenter().getY()))**2) <= (detstars[i].getRadius()**2):
                    points += 15
                    detstars[i].undraw()
                    detonators.append(i)
                    del detstars[i]
                    detonator()

            #Check if detonators are activated
            todel2 = []
            todel3 = []
            todel4 = []
            if len(clickdets) > 0:
                for i in range(len(clickdets)):
                    #If detonator is clicked. Delete all balls
                    if len(balls) > 0:
                        if ((x - (clickdets[i].getCenter().getX()))**2 + (y - (clickdets[i].getCenter().getY()))**2) <= (clickdets[i].getRadius()**2):
                            detlength = len(clickdets) - 1
                            clickdets[detlength].undraw()
                            todel3.append(clickdets[detlength])
                            clickdetbomb[detlength].undraw()
                            todel4.append(clickdetbomb[detlength])
                            for i in range(len(balls)):
                                balls[i].undraw()
                                todel2.append(balls[i])
                            for ball in todel2:
                                balls.remove(ball)
                                points += 9
                            for clickdet in todel3:
                                clickdets.remove(clickdet)
                            for clickdetb in todel4:
                                clickdetbomb.remove(clickdetb)
                            win.update()
                            stall()
                            
            if x < 35 and y < 152 and y > 73:
                paused()
            if x < 35 and y < 70:
                about()
                        
        #Update points and timecheck
        if timecheck % 4 == 0:
            points += 1
        txtpoints.setText(points)
        timecheck += 1
        win.update()
        time.sleep(.1/2)
        
    t = Text(Point(300, 150), "GAME OVER")
    t.setSize(20)
    t.draw(win)
    HighScores()
    win.update()
    win.close()
