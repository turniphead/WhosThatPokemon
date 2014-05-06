'''
CIS 192 Final Project: Pokemon Quiz
'''
import pygame
import wx
import math
import time
import random

class WhosThatPokemon(wx.Frame):
    
    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)
    
        #Create pointers to pokemon pics
        self.num2name = {}
        self.num2color = {}
        self.num2black = {}
        f = open('Names.txt','r')
        for line in f.read().splitlines():
            split = line.split('-')
            self.num2name[int(split[0])] = split[1]
            self.num2color[int(split[0])] = line+'.png'
            self.num2black[int(split[0])] = line+'-s.png'
        f.close()

        self.curr = random.randint(1,151)
        #Initialize game values
        self.score = 0
        self.time = 0
        self.points = 10
        self.pause = False

        #Choose and draw first picture
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap('color/' + self.num2color[self.curr], wx.BITMAP_TYPE_PNG))
        self.GetSizer().Add(item=self.png, proportion=1) 
        
        #Create timer, start
        self.Timer = wx.Timer(self)
        self.Timer.Start(1000)

        #Call necessary interface methods
        self.CreateTextCtrl()
        self.CreateMenuButtons()
        sizer.Fit(self)
        
    def playFile(self,event):
        pygame.mixer.init()
        pygame.mixer.music.load('Music/poke.wav')
        pygame.mixer.music.play()

    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT, handler=self.Enter, source=text)
        self.text = text   

    def Enter(self, event):
        key = event.GetEventObject().GetValue()
        if(self.points == 0.0):
            self.NextPokemon()
        if(key == self.num2name[self.curr] and not self.pause):
            self.score += self.points
            self.score_button.SetLabel("Score: " + str(self.score))
            self.NextPokemon()
    
    def NextPokemon(self):
            self.points = 10
            self.curr = random.randint(1,151)
            self.png.SetBitmap(wx.Bitmap('color/' + self.num2color[self.curr]))
            self.text.Clear()


    def CreateMenuButtons(self):
        gs = wx.GridSizer(3,2)

        self.timer_button = wx.Button(parent=self, label='Time: ' + str(self.time))
        pause = wx.Button(parent=self, label='Pause')
        self.score_button = wx.Button(parent=self, label='Score: ' + str(self.score))
        self.points_button = wx.Button(parent=self, label='Points: ' + str(self.points))
        quit = wx.Button(parent=self, label='Quit')
        restart = wx.Button(parent=self, label='Restart')

        gs.Add(item=self.timer_button, flag=wx.EXPAND)
        gs.Add(item=pause, flag=wx.EXPAND)
        gs.Add(item=self.score_button, flag=wx.EXPAND)
        gs.Add(item=self.points_button, flag=wx.EXPAND)
        gs.Add(item=quit, flag=wx.EXPAND)
        gs.Add(item=restart, flag=wx.EXPAND)
        
        
        self.Bind(wx.EVT_TIMER, self.update_timer, self.Timer)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Pause, source=pause)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Restart, source=restart)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)

        self.play = wx.Button(parent=self,label="Play")
        self.play.Bind(wx.EVT_BUTTON, self.playFile)

    
    def Quit(self, event):
        self.Destroy()    

    def update_timer(self, event):
        if(self.pause == False):
            self.time += 1
            if (self.points > 0):
                self.points -= 0.5
        self.timer_button.SetLabel("Time: " + str(self.time))
        self.points_button.SetLabel("Points: " + str(self.points))
        if(self.points == 0): 
            self.NextPokemon()
        
    def Pause(self, event):
        self.pause = not (self.pause)    

    def Restart(self, event):
        self.time = 0
        self.score = 0
        self.points = 10
        self.points_button.SetLabel("Points: " + str(self.points))
        self.score_button.SetLabel("Score: " + str(self.score))
        self.timer_button.SetLabel("Time: " + str(self.time))



def main():
    app = wx.App()
    frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title='Who Is That Pokemon?')
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
