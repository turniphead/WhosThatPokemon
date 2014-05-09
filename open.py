import wx
import game
class Instructions(wx.Frame):
    def __init__(self, *args, **keywords):
        wx.Frame.__init__(self, *args, **keywords)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        Background = wx.StaticBitmap(self, -1, wx.Bitmap('Intro.png', wx.BITMAP_TYPE_ANY))
        sizer.Add(item=Background, flag=wx.EXPAND)
        self.MakeButtons()
        sizer.Fit(self)
    def MakeButtons(self):
        gs = wx.GridSizer(1,2)

        start = wx.Button(parent=self, label="I'm ready!")
        quit = wx.Button(parent=self, label="I'm not ready yet!")

        gs.Add(item=start, flag=wx.EXPAND)
        gs.Add(item=quit, flag=wx.EXPAND)

        self.Bind(event=wx.EVT_BUTTON, handler=self.GoToGame, source=start)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)
    
    def GoToGame(self, event):
        self.Destroy()
        game.main()
        

    def Quit(self, event):
        self.Destroy()

def main():
    app = wx.App()
    frame1 = Instructions(parent=None, id=wx.ID_ANY, title="Who's That Pokemon?")
    frame1.Show(True)
    frame1.Center()
    frame1.SetFocus()
    app.MainLoop()

if __name__ == "__main__":
    main()
        


