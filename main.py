'''
CIS 192 Final Project: Pokemon Quiz
'''

import wx
import math
import time
class WhosThatPokemon(wx.Frame):

    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)
        
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("pik.jpg", wx.BITMAP_TYPE_ANY))
        self.GetSizer().Add(item=self.png, proportion=1) 
        self.score = 0
        self.time = 0
        self.points = 10
        self.pause = False
        self.Timer = wx.Timer(self)
        self.Timer.Start(1000)
        self.CreateTextCtrl()
        self.CreateMenuButtons()
        sizer.Fit(self)
  
    
    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT, handler=self.Enter, source=text)
        self.text = text   

    def Enter(self, event):
        key = event.GetEventObject().GetValue()
        if(key == 'Pikachu' and not self.pause):
            self.score += self.points
            self.score_button.SetLabel("Score: " + str(self.score))
            self.points = 10


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
    
    def Quit(self, event):
        self.Destroy()    

    def update_timer(self, event):
        if(self.pause == False):
            self.time += 1
            if (self.points > 0):
                self.points -= 0.5
        self.timer_button.SetLabel("Time: " + str(self.time))
        self.points_button.SetLabel("Points: " + str(self.points))
        
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
