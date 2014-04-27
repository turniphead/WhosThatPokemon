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
        self.time = time.clock()
        self.CreateTextCtrl()
        self.CreateMenuButtons()
        sizer.Fit(self)
  
    
    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT_ENTER, handler=self.Enter, source=text)
        self.text = text   

    def Enter(self, event):
        b = event.GetEventObject().GetLabel()

    def CreateMenuButtons(self):
        gs = wx.GridSizer(1,2)
        quit = wx.Button(parent=self, label='Quit')
        restart = wx.Button(parent=self, label='Time: ' + str(self.time))

        gs.Add(item=quit, flag=wx.EXPAND)
        gs.Add(item=restart, flag=wx.EXPAND)

        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Restart, source=restart)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)
    
    def Quit(self, event):
        wx.GetApp().ExitMainLoop()
    def Restart(self, event):
        self.score = 0
        self.time = 0
        

def main():
    app = wx.App()
    frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title='Who Is That Pokemon?')
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
