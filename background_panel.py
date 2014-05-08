import wx

class BackPanel(wx.Panel):

    def __init__(self, parent, poke_img_name):
        wx.Panel.__init__(self, parent, size = (454, 340) )
        self.Bind(wx.EVT_PAINT, self.OnPaint)

        self.back = wx.Bitmap("background_img.png", wx.BITMAP_TYPE_PNG)
        self.poke = wx.Bitmap(poke_img_name)


    def OnPaint(self, evt):
        dc = wx.PaintDC(self)
        dc.SetBackground(wx.Brush("WHITE"))

        # ... drawing here all other images in order of overlapping
        dc.DrawBitmap(self.back, 0, 0, True)
        dc.DrawBitmap(self.poke, 0, 0, True)