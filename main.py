'''
CIS 192 Final Project: Pokemon Quiz
'''

import wx
import math
class Calculator(wx.Frame):

    def __init__(self, *args, **keywords):

        wx.Frame.__init__(self, *args, **keywords)
        
        sizer = wx.BoxSizer(orient=wx.VERTICAL)
        self.SetSizer(sizer)
        self.png = wx.StaticBitmap(self, -1, wx.Bitmap("3.gif", wx.BITMAP_TYPE_ANY))
        self.GetSizer().Add(item=self.png, proportion=1) 
        self.history = {}
        self.instruction = 0

        self.CreateTextCtrl()
        self.CreateUndoRedo()
        sizer.Fit(self)
  
    
    def CreateTextCtrl(self):
        text = wx.TextCtrl(self)
        self.GetSizer().Add(item=text, flag=wx.EXPAND)
        self.Bind(event=wx.EVT_TEXT_ENTER, handler=self.Enter, source=text)
        self.text = text   

    def Enter(self, event):
        b = event.GetEventObject().GetLabel()
        self.history[self.instruction] = self.text.GetValue()
        self.instruction += 1
        if b == wx.WXK_RETURN:
            self.text.Clear()
        else:
            self.text.AppendText(b)

    def CreateUndoRedo(self):
        gs = wx.GridSizer(1,2)
        undo = wx.Button(parent=self, label='Undo')
        redo = wx.Button(parent=self, label='Redo')

        gs.Add(item=undo, flag=wx.EXPAND)
        gs.Add(item=redo, flag=wx.EXPAND)

        self.Bind(event=wx.EVT_BUTTON, handler=self.Undo, source=undo)
        self.Bind(event=wx.EVT_BUTTON, handler=self.Redo, source=redo)

        self.GetSizer().Add(item=gs, flag=wx.EXPAND)
    
    def Undo(self, event):
        if self.instruction > 0:
            self.instruction -= 1
            self.text.ChangeValue(self.history[self.instruction]) 

    def Redo(self, event):
        if self.instruction < (len(self.history) - 1):
            self.instruction += 1
            self.text.ChangeValue(self.history[self.instruction])        

def main():
    app = wx.App()
    frame = Calculator(parent=None, id=wx.ID_ANY, title='Who Is That Pokemon?')
    frame.Show(True)
    app.MainLoop()


if __name__ == "__main__":
    main()
