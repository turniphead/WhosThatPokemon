# create a background image on a wxPython panel
# and show a button on top of the image
 
import wx
 
class BackPanel(wx.Panel):
    """class Panel1 creates a panel with an image on it, inherits wx.Panel"""
    def __init__(self, parent, id):
        # create the panel
        wx.Panel.__init__(self, parent, id)
        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = 'background_img.png'
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.bitmap1 = wx.StaticBitmap(self, -1, bmp1, (0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight()) 
            parent.SetTitle(str1)
        except IOError:
            print "Image file %s not found" % imageFile
            raise SystemExit
 
        # button goes on the image --> self.bitmap1 is the parent
        #self.button1 = wx.Button(self.bitmap1, id=-1, label='Button1', pos=(8, 8))

