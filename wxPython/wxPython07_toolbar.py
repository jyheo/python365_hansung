import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Toolbar Example'
        self.SetTitle(self.title)
        self.initToolbar()
        self.initStatusBar()
        self.Center()
        self.Show()

    def initToolbar(self):
        self.toolbar = self.CreateToolBar(style=wx.TB_TEXT)
        newtool = self.toolbar.AddLabelTool(wx.ID_NEW, 'New', wx.Bitmap('new.png'))
        self.toolbar.AddLabelTool(wx.ID_BACKWARD, 'Backward', wx.Bitmap('back.png'))
        self.toolbar.AddLabelTool(wx.ID_HOME, 'Home', wx.Bitmap('home.png'))
        self.toolbar.AddLabelTool(wx.ID_FORWARD, 'Forward', wx.Bitmap('forward.png'))
        self.toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.onNew, newtool)

    def initStatusBar(self):
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText('Ready')

    def onNew(self, e):
        print 'New toolbar pressed'
            
def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
