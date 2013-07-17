import wx

class MainFrame(wx.Frame):
    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.SetTitle('Frame Example')
        self.Center()
        self.Show()

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
