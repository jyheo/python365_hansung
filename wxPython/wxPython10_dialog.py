import wx

class ChangeDepthDialog(wx.Dialog):
    
    def __init__(self, *args, **kw):
        super(ChangeDepthDialog, self).__init__(*args, **kw) 
            
        self.InitUI()
        self.SetSize((250, 200))
        self.SetTitle("Change Color Depth")
        
        
    def InitUI(self):

        pnl = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        sb = wx.StaticBox(pnl, label='Colors')
        sbs = wx.StaticBoxSizer(sb, orient=wx.VERTICAL)        
        sbs.Add(wx.RadioButton(pnl, label='256 Colors', 
            style=wx.RB_GROUP))
        sbs.Add(wx.RadioButton(pnl, label='16 Colors'))
        sbs.Add(wx.RadioButton(pnl, label='2 Colors'))
        
        hbox1 = wx.BoxSizer(wx.HORIZONTAL)        
        hbox1.Add(wx.RadioButton(pnl, label='Custom'))
        hbox1.Add(wx.TextCtrl(pnl), flag=wx.LEFT, border=5)
        sbs.Add(hbox1)
        
        pnl.SetSizer(sbs)
       
        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        okButton = wx.Button(self, label='Ok')
        closeButton = wx.Button(self, label='Close')
        hbox2.Add(okButton)
        hbox2.Add(closeButton, flag=wx.LEFT, border=5)

        vbox.Add(pnl, proportion=1, 
            flag=wx.ALL|wx.EXPAND, border=5)
        vbox.Add(hbox2, 
            flag=wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, border=10)

        self.SetSizer(vbox)
        
        okButton.Bind(wx.EVT_BUTTON, self.OnClose)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        
        
    def OnClose(self, e):
        
        self.Destroy()

class MainFrame(wx.Frame):

    def __init__(self):
        super(MainFrame, self).__init__(None)

        self.SetTitle('Button Example')
        self.initWidget()
        self.Center()
        self.Show()

    def initWidget(self):
        btn = wx.Button(self, id=wx.NewId(), label='Hello')
        btn.Bind(wx.EVT_BUTTON, self.onHello)

    def onHello(self, event):
        chgdep = ChangeDepthDialog(None, 
            title='Change Color Depth')
        chgdep.ShowModal()
        chgdep.Destroy()
       

def main():
    app = wx.App(redirect=False)
    MainFrame()
    app.MainLoop()

if __name__ == '__main__':
    main()
