import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Statusbar Example'
        self.SetTitle(self.title)
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        panel = wx.Panel(self)

        # Radio Button
        self.rb1 = wx.RadioButton(panel, label='Value A', pos=(10, 10), 
            style=wx.RB_GROUP)
        self.rb2 = wx.RadioButton(panel, label='Value B', pos=(10, 30))
        self.rb3 = wx.RadioButton(panel, label='Value C', pos=(10, 50))
        
        self.rb1.Bind(wx.EVT_RADIOBUTTON, self.onSetVal)
        self.rb2.Bind(wx.EVT_RADIOBUTTON, self.onSetVal)
        self.rb3.Bind(wx.EVT_RADIOBUTTON, self.onSetVal)

        # Status Bar
        self.sb = self.CreateStatusBar(3)
        
        self.sb.SetStatusText("True", 0)
        self.sb.SetStatusText("False", 1)
        self.sb.SetStatusText("False", 2)  

    def onSetVal(self, e):
        state1 = str(self.rb1.GetValue())
        state2 = str(self.rb2.GetValue())
        state3 = str(self.rb3.GetValue())

        self.sb.SetStatusText(state1, 0)
        self.sb.SetStatusText(state2, 1)
        self.sb.SetStatusText(state3, 2)          

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
