import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Checkbox Example'
        self.SetTitle(self.title)
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        panel = wx.Panel(self)

        cb = wx.CheckBox(panel, label='Show title', pos=(20, 20))
        cb.SetValue(True)

        cb.Bind(wx.EVT_CHECKBOX, self.onShowOrHideTitle)

    def onShowOrHideTitle(self, e):
        sender = e.GetEventObject()
        isChecked = sender.GetValue()
        
        if isChecked:
            self.SetTitle(self.title)            
        else: 
            self.SetTitle('')         

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
