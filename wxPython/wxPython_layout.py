import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.SetTitle('Layout Example')
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        panel = wx.Panel(self)

        panel.SetBackgroundColour('gray')
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox = wx.BoxSizer(wx.HORIZONTAL)

        pans = [wx.Panel(panel), wx.Panel(panel), wx.Panel(panel)]
        pans[0].SetBackgroundColour('blue')
        pans[1].SetBackgroundColour('green')
        pans[2].SetBackgroundColour('red')

        vbox.Add(pans[0], flag=wx.EXPAND)
        vbox.Add(hbox, flag=wx.EXPAND)
        hbox.Add(pans[1], flag=wx.EXPAND)
        hbox.Add(pans[2], flag=wx.EXPAND)
        
        panel.SetSizer(vbox)

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
