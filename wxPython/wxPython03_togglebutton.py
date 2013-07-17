import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'ToggleButton Example'
        self.SetTitle(self.title)
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        self.red, self.green, self.blue = 0, 0, 0

        panel = wx.Panel(self)
        rtb = wx.ToggleButton(panel, label='red', pos=(20, 25))
        gtb = wx.ToggleButton(panel, label='green', pos=(20, 60))
        btb = wx.ToggleButton(panel, label='blue', pos=(20, 100))
        self.cpnl  = wx.Panel(panel, pos=(150, 20), size=(110, 110))
        self.cpnl.SetBackgroundColour(wx.Colour(self.red, self.green, self.blue))

        rtb.Bind(wx.EVT_TOGGLEBUTTON, self.onChangeColor)
        gtb.Bind(wx.EVT_TOGGLEBUTTON, self.onChangeColor)
        btb.Bind(wx.EVT_TOGGLEBUTTON, self.onChangeColor)

    def onChangeColor(self, e):
        obj = e.GetEventObject()
        isPressed = obj.GetValue()
        label = obj.GetLabelText()
        
        if not label in ['red', 'green', 'blue']:
            return

        if isPressed:
            setattr(self, label, 255)
        else:
            setattr(self, label, 0)
            
        self.cpnl.SetBackgroundColour(wx.Colour(self.red, self.green, self.blue))
        self.cpnl.Refresh()

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
