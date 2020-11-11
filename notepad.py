import wx
import os

WIDTH = 500
HEIGHT = 400

class Window(wx.Frame):
 
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(WIDTH, HEIGHT))
        self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.Show(True)
        
        
        menubar = wx.MenuBar()
 
        file_menu = wx.Menu()
        openItem = file_menu.Append(wx.ID_OPEN,"Open","Push the button to Open file")
        saveItem = file_menu.Append(wx.ID_SAVE,"Save","Push the button to Save file")
        exitItem = file_menu.Append(wx.ID_EXIT,"Exit","Push the button to leave this application")
        #bar = wx.MenuBar()
        menubar.Append(file_menu,"File")
        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_MENU, self.OnOpen, openItem)
        self.Bind(wx.EVT_MENU, self.OnSave, saveItem)
        self.Bind(wx.EVT_MENU, self.OnExit, exitItem)
        
        
        help_menu = wx.Menu()
        aboutItem = help_menu.Append(wx.ID_ABOUT,"About","Push the button to get an information about this application")
        menubar.Append(help_menu,"Help")
        self.Bind(wx.EVT_MENU, self.OnAbout, aboutItem)
        
        
        
 
    def OnAbout(self, e):
        dlg = wx.MessageDialog(self, "This is a mini editor keeping your text","About pyNote", wx.OK)
        dlg.ShowModal()
    
    def OnOpen(self, e):
        with wx.FileDialog(self, "Open TXT file", wildcard="TXT files (*.txt)|*.txt",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            
            # Proceed loading the file chosen by the user
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    self.LoadFile(file)
            except IOError:
                wx.LogError("Cannot open file '%s'." % newfile)
    
    def OnSave(self, e):
        pass
    
    def OnExit(self, e):
        exit()
    
    def LoadFile(self, file):
        
        self.control.AppendText(file.read())
        #self.control.AppendText("Some another Text\n")

app = wx.App()
wnd = Window(None, "pyNote")
app.MainLoop()
