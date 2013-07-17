import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.SetTitle('Button Example')
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        # 1. Create Button
        btn = wx.Button(self, label='Hello')

        # 2. Bind button click event
        btn.Bind(wx.EVT_BUTTON, self.onHello)

    def onHello(self, event):
        btn = event.GetEventObject()
        print 'Button pressed:', btn.GetLabelText()
       

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
