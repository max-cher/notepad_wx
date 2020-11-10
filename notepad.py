import wx
import os
 
class Window(wx.Frame):
 
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(300,250))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)
 
        menu = wx.Menu()
        aboutItem = menu.Append(wx.ID_ABOUT,"About","Push the button to get an information about this application")
        openItem = menu.Append(wx.ID_OPEN,"Open","Push the button to Open file")
        exitItem = menu.Append(wx.ID_EXIT,"Exit","Push the button to leave this application")
        bar = wx.MenuBar()
        
        bar.Append(menu,"File")
        self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        
        self.Bind(wx.EVT_MENU, self.OnExit, openItem)
        #bar.Append(menu,"Open")
        #self.SetMenuBar(bar)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
 
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "This is a mini editor keeping your text","About pyNote", wx.OK)
        dlg.ShowModal()
    
    def OnOpen(self, e):
        exit()
    
    def OnExit(self, e):
        exit()

app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()
