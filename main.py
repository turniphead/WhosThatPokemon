'''
CIS 192 Final Project: Pokemon Quiz
'''
import pygame
import wx
import math
import time
import random
from background_panel import *

class WhosThatPokemon(wx.Frame):
    
    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)

        only_one_pokemon = False
    
        #Create pointers to pokemon pics
        self.num2name = {}
        self.num2color = {}
        self.num2black = {}
        f = open('Names.txt','r')
        for line in f.read().splitlines():
            split = line.split('-')
            self.num2name[int(split[0])] = split[1]
            if (not only_one_pokemon or (int(split[0]) == 1) ):
                self.num2color[int(split[0])] = line+'.png'
                self.num2black[int(split[0])] = line+'-s.png'
        f.close()

        self.curr = random.randint(1,151)  #sometimes -1 or -2

        if (only_one_pokemon):
            self.curr = 1
        #Initialize game values
        self.score = 0
        self.time = 0
        self.points = 10
        self.pause = False
        self.music = "off" # has 4 values: off, playing, paused, paused_duetogame
        self.easy = False


        #create background image and first pokemon, without returning error
        no_log = wx.LogNull()
        self.back_panel = BackPanel(self,'black/' + self.num2black[self.curr])
        del no_log

        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        self.GetSizer().Add(item=self.back_panel)
        
        #Create timer, start
        self.Timer = wx.Timer(self)
        self.Timer.Start(1000)

        #Call necessary interface methods
        self.CreateTextCtrl()
        self.CreateMenuButtons()
        sizer.Fit(self)
        self.text.SetFocus()
        
    # music button method
    def playFile(self,event):
        if (not self.pause):
            if (self.music == "playing"):
                pygame.mixer.music.pause()
                self.music = "paused"
                self.music_button.SetLabel("Resume Music")
            elif (self.music == "paused"):
                pygame.mixer.music.unpause()
                self.music = "playing"
                self.music_button.SetLabel("Pause Music")
            elif (self.music == "off"):
                pygame.mixer.init()
                pygame.mixer.music.load('Music/poke.wav')
                pygame.mixer.music.play(loops=-1)
                self.music = "playing"
                self.music_button.SetLabel("Pause Music")
        self.text.SetFocus()

    # textbox method
    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT, handler=self.Enter, source=text)
        self.text = text   

    # method called everytime textbox text is edited
    def Enter(self, event):
        key = event.GetEventObject().GetValue()
        if (self.curr != -2):
            if(self.points == 0.0):
                self.NextPokemon()
            if(key.lower() == self.num2name[self.curr].lower() and not self.pause):
                self.score += self.points
                self.score_button.SetLabel("Score: " + str(self.score))
                self.NextPokemon()
    
    # pokemon picture change method
    def NextPokemon(self):
            # delete the current pokemon from both sets of pokemon
            if (self.curr >= 0):
                del self.num2color[self.curr]
                del self.num2black[self.curr]

            keys_left = self.num2color.keys()
            if (len(keys_left) == 0):
                self.curr = -2
                self.back_panel.poke = wx.Bitmap('end.jpg')
                self.back_panel.Refresh()
                self.text.Clear()
                self.text.AppendText('Congratulations, you win!')
                self.text.SetEditable(False)
                return

            self.curr = keys_left[ random.randint(0,len(keys_left)-1) ]

            if(self.easy):
                self.back_panel.poke = wx.Bitmap('color/' + self.num2color[self.curr])
            else:
                self.back_panel.poke = wx.Bitmap('black/' + self.num2black[self.curr])

            self.points = 10
            self.back_panel.Refresh()
            self.text.Clear()

    # initialize all buttons, called once at beginning of script
    def CreateMenuButtons(self):
        gs = wx.GridSizer(4,2)

        self.timer_button = wx.Button(parent=self, label='Time: ' + str(self.time))
        self.pause_button = wx.Button(parent=self, label='Pause')
        self.score_button = wx.Button(parent=self, label='Score: ' + str(self.score))
        self.points_button = wx.Button(parent=self, label='Points: ' + str(self.points))
        quit = wx.Button(parent=self, label='Quit')
        restart = wx.Button(parent=self, label='Restart')
        self.music_button = wx.Button(parent=self,label="Play Music")
        self.easy_button = wx.Button(parent=self,label="Easy Mode: OFF")

        gs.Add(item=self.timer_button, flag=wx.EXPAND)
        gs.Add(item=self.pause_button, flag=wx.EXPAND)
        gs.Add(item=self.score_button, flag=wx.EXPAND)
        gs.Add(item=self.points_button, flag=wx.EXPAND)
        gs.Add(item=quit, flag=wx.EXPAND)
        gs.Add(item=restart, flag=wx.EXPAND)
        gs.Add(item=self.music_button, flag=wx.EXPAND)
        gs.Add(item=self.easy_button, flag=wx.EXPAND)
        
        self.Bind(wx.EVT_TIMER, self.update_timer, self.Timer)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Pause, source=self.pause_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Restart, source=restart)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)
        self.Bind(event=wx.EVT_BUTTON, handler=self.playFile, source=self.music_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.change_difficulty, source=self.easy_button)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)

    # called when the easy button is pressed. changes difficulty
    def change_difficulty(self, event):
        self.easy = not self.easy
        if (self.easy):
            self.easy_button.SetLabel('Easy Mode: ON')
            self.back_panel.poke = wx.Bitmap('color/' + self.num2color[self.curr])
        else:
            self.easy_button.SetLabel('Easy Mode: OFF')
            self.back_panel.poke = wx.Bitmap('black/' + self.num2black[self.curr])
        self.back_panel.Refresh()
        self.text.SetFocus()


    # quit button method
    def Quit(self, event):
        if (self.music != "off"):
            pygame.mixer.music.stop()
        self.Destroy()
        return

    # timer event, called once per second
    def update_timer(self, event):
        if(self.pause == False):
            self.time += 1
            if (self.points > 0):
                self.points -= 0.5
        self.timer_button.SetLabel("Time: " + str(self.time))
        self.points_button.SetLabel("Points: " + str(self.points))
        if(self.points == 0): 
            self.NextPokemon()
        
    # pause button method
    def Pause(self, event):
        self.pause = not (self.pause)

        if self.pause:
            self.pause_button.SetLabel("Unpause")
            self.text.SetEditable(False)
        else:
            self.pause_button.SetLabel("Pause")
            self.text.SetEditable(True)

        if(self.music != "off"):
            # pause music if you pause the game
            if(self.pause and self.music=="playing"):
                pygame.mixer.music.pause()
                self.music = "paused_duetogame"
            # start playing music when game unpauses, 
            # but only if it was paused by the game in the first place
            elif ( (not self.pause) and self.music == "paused_duetogame"):
                pygame.mixer.music.unpause()
                self.music = "playing"
        self.text.SetFocus()


    def Restart(self, event):
        # reset pokemon lists
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

        # tells next pokemon to not delete the current pokemon from the set
        self.curr = -1
        self.NextPokemon()

        self.time = 0
        self.score = 0
        self.points_button.SetLabel("Points: " + str(self.points))
        self.score_button.SetLabel("Score: " + str(self.score))
        self.timer_button.SetLabel("Time: " + str(self.time))

        self.text.SetEditable(True)
        self.text.SetFocus()



def main():
    app = wx.App()
    frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title='Who Is That Pokemon?')
    frame.Show(True)
    frame.SetFocus()
    app.MainLoop()


if __name__ == "__main__":
    main()
