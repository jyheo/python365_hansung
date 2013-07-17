import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.SetTitle('Panel Example')
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        # 1. Create Panel
        panel = wx.Panel(self)

        # 2. Create button on Panel
        btn = wx.Button(panel, label='Hello1', pos=(20,30))
        btn.Bind(wx.EVT_BUTTON, self.onHello)

        wx.Button(panel, label='Hello2', pos=(20,60)).Bind(wx.EVT_BUTTON, self.onHello)
        wx.Button(panel, label='Hello3', pos=(20,90)).Bind(wx.EVT_BUTTON, self.onHello)

    def onHello(self, event):
        btn = event.GetEventObject()
        print 'Button pressed:', btn.GetLabelText()
       

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
