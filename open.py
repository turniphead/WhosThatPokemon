''' The introduction screen that allows the user to either start the game or quit. '''
import wx
import pygame
import game

class Instructions(wx.Frame):

    def __init__(self, *args, **keywords):
        #Create frame and sizer 
        wx.Frame.__init__(self, *args, **keywords)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)

        #Background image
        Background = wx.StaticBitmap(self, -1, wx.Bitmap('Intro.png', wx.BITMAP_TYPE_ANY))
        sizer.Add(item=Background, flag=wx.EXPAND)
        self.MakeButtons()
        sizer.Fit(self)
        pygame.mixer.init()
        pygame.mixer.music.load('Music/intro.wav')
        pygame.mixer.music.play()

    def MakeButtons(self):
        #Create grid sizer for buttons
        gs = wx.GridSizer(1,2)

        #Create buttons
        start = wx.Button(parent=self, label="I'm ready!")
        quit = wx.Button(parent=self, label="I'm not ready yet!")

        #Add buttons to grid sizer
        gs.Add(item=start, flag=wx.EXPAND)
        gs.Add(item=quit, flag=wx.EXPAND)

        #Bind button pushes to correct method calls
        self.Bind(event=wx.EVT_BUTTON, handler=self.GoToGame, source=start)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Quit, source=quit)

        #Add grid sizer to the sizer
        self.GetSizer().Add(item=gs, flag=wx.EXPAND)
    
    def GoToGame(self, event):
        self.Destroy()

        #Calls the main method of game.py
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
        


