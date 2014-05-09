import wx
from main import *

class Instructions(wx.Frame):
	def __init__(self, *args, **keywords):
		wx.Frame.__init__(self, *args, **keywords)
		fi = open('instructions.txt','r')
		self.instr = fi.read()
		fi.close()
		sizer = wx.BoxSizer(orient=wx.VERTICAL)
		self.SetSizer(sizer)
		self.MakeText()
		self.MakeButton()

	def MakeText(self):
		self.text = wx.TextCtrl(self, value=self.instr, style = wx.TE_MULTILINE|wx.TE_READONLY|wx.EXPAND, size=(500,250))
		self.GetSizer().Add(item=self.text, flag=wx.EXPAND)

	def MakeButton(self):
		self.button = wx.Button(parent=self, label="I'm Ready!")
		self.Bind(event=wx.EVT_BUTTON, handler=self.GoToGame, source=self.button)
		self.GetSizer().Add(item=self.button, flag=wx.EXPAND)

	def GoToGame(self,event):
		self.Destroy()
		#os.system('python main.py')
		frame = WhosThatPokemon(parent=None, id=wx.ID_ANY, title="Who's That Pokemon?")
		frame.Show(True)
		frame.Center()
		frame.SetFocus()
		frame.text.SetFocus()

def main():
    app = wx.App()
    frame1 = Instructions(parent=None, id=wx.ID_ANY, title="Who's That Pokemon?", size = (500,315))
    frame1.Show(True)
    frame1.Center()
    frame1.SetFocus()
    app.MainLoop()


if __name__ == "__main__":
    main()