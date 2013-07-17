import wx

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.title = 'Combobox Example'
        self.SetTitle(self.title)
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        panel = wx.Panel(self)

        pythons = ['Tkinter', 'wxPython', 'PyGTK', 'PyQT', 'PySide']
        cb = wx.ComboBox(panel, pos=(50, 30), choices=pythons, 
            style=wx.CB_READONLY)

        self.st = wx.StaticText(panel, label='', pos=(50, 140))
        cb.Bind(wx.EVT_COMBOBOX, self.onSelect)

    def onSelect(self, e):
        i = e.GetString()
        self.st.SetLabel(i)   

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
