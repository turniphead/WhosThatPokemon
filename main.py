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


        fi = open('instructions.txt','r')
        instr = fi.read()
        fi.close()
        #wx.MessageBox(instr, 'Instructions', wx.OK | wx.ICON_INFORMATION)
        
        #m = wx.MessageDialog(self,instr,'Instructions',  wx.OK | wx.ICON_INFORMATION)
        #m.ShowModal()
        #m.Destroy()

        only_one_pokemon = True

        pygame.mixer.init()
        pygame.mixer.music.load('Music/poke-who.wav')
        pygame.mixer.music.play()

    
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
        self.hint = False


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

        # Make hidden textbox for hint
        self.hint_text = wx.TextCtrl(self)
        self.hint_text.SetEditable(False)
        self.GetSizer().Add(item=self.hint_text, flag=wx.EXPAND)
        #self.GetSizer().Hide(self.hint_text)

        self.GetSizer().Fit(self)

        self.text.SetFocus()
        
    # textbox method
    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT, handler=self.Enter, source=text)
        self.text = text

    # initialize all buttons, called once at beginning of script
    def CreateMenuButtons(self):
        gs = wx.GridSizer(5,2)

        self.timer_button = wx.Button(parent=self, label='Time: ' + str(self.time))
        self.score_button = wx.Button(parent=self, label='Score: ' + str(self.score))
        self.points_button = wx.Button(parent=self, label='Points This Round: ' + str(self.points))
        self.pause_button = wx.Button(parent=self, label='Pause')
        quit = wx.Button(parent=self, label='Quit')
        restart = wx.Button(parent=self, label='Restart')
        self.music_button = wx.Button(parent=self,label="Play Music")
        self.easy_button = wx.Button(parent=self,label="Easy Mode: OFF")
        next = wx.Button(parent=self,label="Next Pokemon")
        self.hint_button = wx.Button(parent=self,label="Show Hint")

        gs.Add(item=self.timer_button, flag=wx.EXPAND)
        gs.Add(item=self.score_button, flag=wx.EXPAND)
        gs.Add(item=self.points_button, flag=wx.EXPAND)
        gs.Add(item=self.pause_button, flag=wx.EXPAND)
        gs.Add(item=quit, flag=wx.EXPAND)
        gs.Add(item=restart, flag=wx.EXPAND)
        gs.Add(item=self.music_button, flag=wx.EXPAND)
        gs.Add(item=self.easy_button, flag=wx.EXPAND)
        gs.Add(item=next, flag=wx.EXPAND)
        gs.Add(item=self.hint_button, flag=wx.EXPAND)
        
        self.Bind(wx.EVT_TIMER, self.update_timer, self.Timer)
        self.Bind(event=wx.EVT_BUTTON, handler=self.unclickable_button, source=self.timer_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.unclickable_button, source=self.score_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.unclickable_button, source=self.points_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Pause, source=self.pause_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Restart, source=restart)
        self.Bind(event=wx.EVT_BUTTON, handler=self.playFile, source=self.music_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.change_difficulty, source=self.easy_button)
        self.Bind(event=wx.EVT_BUTTON, handler=self.NextPokemon, source=next)
        self.Bind(event=wx.EVT_BUTTON, handler=self.ShowHideHint, source=self.hint_button)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)

    # method to bind to unclickable buttons to return focus to textbox
    def unclickable_button(self, event):
        self.text.SetFocus()

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
                pygame.mixer.music.load('Music/poke.wav')
                pygame.mixer.music.play(loops=-1)
                self.music = "playing"
                self.music_button.SetLabel("Pause Music")
        self.text.SetFocus()

    
    # pokemon picture change method
    def NextPokemon(self, event=[]):
            # delete the current pokemon from both sets of pokemon
            if (self.curr >= 0):
                del self.num2color[self.curr]
                del self.num2black[self.curr]

            if(self.hint):
                self.ShowHideHint()

            keys_left = self.num2color.keys()
            if (len(keys_left) == 0):
                self.Pause()
                self.curr = -2
                self.back_panel.back = wx.Bitmap('end.jpg')
                self.back_panel.poke = wx.Bitmap('transparent.png')
                self.back_panel.Refresh()
                self.text.Clear()
                self.text.AppendText('Congratulations, you win!')
                self.text.SetEditable(False)
                self.points = 10
                self.points_button.SetLabel("Points This Round: " + str(self.points))

                #high score grabbing
                h = open('high_score.txt','r')
                high_score = float(h.read())
                h.close()
                if (self.score > high_score):
                    h = open('high_score.txt','w')
                    h.write(str(self.score))
                    h.close()
                    high_score = str(self.score)+"\tNEW HIGH SCORE!"
                self.hint_text.AppendText("Your Score: " + str(self.score) + "\tHigh Score: " + str(high_score))
                return

            self.curr = keys_left[ random.randint(0,len(keys_left)-1) ]

            if(self.easy):
                self.back_panel.poke = wx.Bitmap('color/' + self.num2color[self.curr])
            else:
                self.back_panel.poke = wx.Bitmap('black/' + self.num2black[self.curr])

            self.points = 10
            self.points_button.SetLabel("Points This Round: " + str(self.points))
            self.back_panel.Refresh()

            
            self.text.Clear()
            self.text.SetFocus()

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

            # updates hint if true and if it's been two seconds
            if (self.hint and self.curr >= 0):
                t = self.time-self.hint_time
                if ( t % 2 == 0 and \
                    t / 2 < len(self.num2name[self.curr])):
                    #self.hint_text.SetEditable(True)
                    self.hint_text.AppendText(self.num2name[self.curr][t/2])
                    #self.hint_text.SetEditable(False)

            self.time += 1

            if (self.points > 0):
                self.points -= 0.5

        self.timer_button.SetLabel("Time: " + str(self.time))
        self.points_button.SetLabel("Points This Round: " + str(self.points))
        if(self.points == 0): 
            self.NextPokemon()
        
    # pause button method
    def Pause(self, event=[]):
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

        self.curr = random.randint(1,151)

        no_log = wx.LogNull()
        self.back_panel.back = wx.Bitmap("background_img.png")
        if(self.easy):
            self.back_panel.poke = wx.Bitmap('color/' + self.num2color[self.curr])
        else:
            self.back_panel.poke = wx.Bitmap('black/' + self.num2black[self.curr])
        self.back_panel.Refresh()
        del no_log

        if (self.pause):
            self.Pause()

        if (self.hint):
            self.ShowHideHint()

        self.time = 0
        self.score = 0
        self.points_button.SetLabel("Points This Round: " + str(self.points))
        self.score_button.SetLabel("Score: " + str(self.score))
        self.timer_button.SetLabel("Time: " + str(self.time))

        self.text.Clear()
        self.text.SetEditable(True)
        self.text.SetFocus()

    def ShowHideHint(self, event=[]):
        self.hint = not self.hint

        if (self.hint):
            self.hint_button.SetLabel("Hide Hint")
            self.hint_text.Clear()
            self.hint_text.AppendText("Hint: ")
            #self.GetSizer().Show(self.hint_text)
            #self.GetSizer().Fit(self)

            self.hint_time = self.time
        else:
            self.hint_button.SetLabel("Show Hint")
            self.hint_text.Clear()
            #self.GetSizer().Hide(self.hint_text)
            #self.GetSizer().Fit(self)

        self.text.SetFocus()


def main():
    app = wx.App()
    frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title="Who's That Pokemon?")
    frame.Show(True)
    frame.Center()
    frame.SetFocus()
    frame.text.SetFocus()
    app.MainLoop()


if __name__ == "__main__":
    main()
