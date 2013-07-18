import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Events'
        self.SetTitle(self.title)
        self.initMenu()
        self.initWidget()
        self.Center()
        self.Show()

    def initMenu(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()

        # file Menu
        fileMenu.Append(wx.ID_NEW, '&New', 'New file')
        fileMenu.Append(wx.ID_OPEN, '&Open', 'Open a file')
        fileMenu.Append(wx.ID_EXIT)

        self.Bind(wx.EVT_MENU, self.onCommand)

        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)

    def initWidget(self):
        panel = wx.Panel(self)
        self.Bind(wx.EVT_KEY_DOWN, self.onKeyDown)
        panel.Bind(wx.EVT_LEFT_DOWN, self.onLeftDown)

        wx.StaticText(panel, label='x:', pos=(10,10))
        wx.StaticText(panel, label='y:', pos=(10,30))
        
        self.st1 = wx.StaticText(panel, label='', pos=(30, 10))
        self.st2 = wx.StaticText(panel, label='', pos=(30, 30))

        # window event
        self.Bind(wx.EVT_MOVE, self.onMove)
        panel.Bind(wx.EVT_SIZE, self.onSize)
        self.Bind(wx.EVT_CLOSE, self.onClose)

    def onCommand(self, e):
        # e is an instance of wx.CommandEvent
        mid = e.GetId()
        if mid == wx.ID_EXIT:
            self.Close()
        elif mid == wx.ID_NEW:
            print 'New'
        elif mid == wx.ID_OPEN:
            print 'Open'

    def onMove(self, e):
        # wx.MoveEvent
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

    def onSize(self, e):
        # wx.SizeEvent
        w, h = e.GetSize()
        print "size", w, h

    def onClose(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question(onClose)',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            
        ret = dial.ShowModal()
        
        if ret == wx.ID_YES:
            self.Destroy()   # Do NOT call self.Close()
        else:
            e.Veto()

    def onKeyDown(self, e):
        # wx.KeyEvent
        key = e.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Are you sure to quit?', 'Question(onKeyDown)', 
                wx.YES_NO | wx.NO_DEFAULT, self)
            if ret == wx.YES:
                self.Close()
        elif key == wx.WXK_UP:
            print 'up'
        else:
            print key
        e.Skip()

    def onLeftDown(self, e):
        # wx.MouseEvent
        print e.GetPosition()
        e.Skip()  # should e.Skip() because it is a focus related event!

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
