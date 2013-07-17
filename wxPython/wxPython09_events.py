import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Events'
        self.SetTitle(self.title)
        self.initWidget()
        self.Center()
        self.Show()

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

    def onMove(self, e):
        x, y = e.GetPosition()
        self.st1.SetLabel(str(x))
        self.st2.SetLabel(str(y))

    def onSize(self, e):
        w, h = e.GetSize()
        print "size", w, h
        e.Skip()

    def onClose(self, e):
        dial = wx.MessageDialog(None, 'Are you sure to quit?', 'Question(onClose)',
            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)
            
        ret = dial.ShowModal()
        
        if ret == wx.ID_YES:
            self.Destroy()   # Do NOT call self.Close()
        else:
            e.Veto()

    def onKeyDown(self, e):
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
        print e.GetPosition()
        e.Skip()

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
