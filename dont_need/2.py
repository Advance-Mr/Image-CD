import wx

class MyFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, title="嵌套滚动面板示例")

        # 创建外层滚动面板
        outer_panel = wx.ScrolledWindow(self)
        outer_panel.SetScrollRate(10, 10)
        outer_sizer = wx.BoxSizer(wx.HORIZONTAL)
        outer_panel.SetSizer(outer_sizer)

        # 创建内层滚动面板
        inner_panel = wx.ScrolledWindow(outer_panel)
        inner_panel.SetScrollRate(10, 10)
        inner_sizer = wx.BoxSizer(wx.VERTICAL)
        inner_panel.SetSizer(inner_sizer)

        # 在内层滚动面板中添加控件
        for i in range(50):
            label = wx.StaticText(inner_panel, label=f"标签{i}")
            inner_sizer.Add(label, 0, wx.ALL, 10)

        # 在外层滚动面板中添加内层滚动面板
        outer_sizer.Add(inner_panel, 1, wx.EXPAND)

app = wx.App()
frame = MyFrame(None)
frame.Show()
app.MainLoop()