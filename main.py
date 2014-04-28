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
        if(key == 
    def CreateMenuButtons(self):
        gs = wx.GridSizer(1,2)
        quit = wx.Button(parent=self, label='Quit')
        time = wx.Button(parent=self, label='Time: ' + str(self.time))
        self.Bind(wx.EVT_TIMER, self.update_timer, self.Timer)

        
        gs.Add(item=quit, flag=wx.EXPAND)
        gs.Add(item=time, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)
    
    def Quit(self, event):
        self.Destroy()    
    def update_timer(self, event):
        self.time += 1
        
             

def main():
    app = wx.App()
    frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title='Who Is That Pokemon?')
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
