import wx

from UI import window

if __name__ == '__main__':
    app = wx.App()
    screen = wx.ScreenDC()
    screen_width, screen_height = screen.GetSize()
    #window.geometry("%dx%d" % (width, height))
    browser = window(None)
    browser.SetSize((int(screen_width*3/4), int(screen_height*3/4)))  # 设置窗口大小to 800x600
    browser.Show()
    app.MainLoop()

    刚才那个界面是以为我电脑太卡了，你原来程序，我没有动，不知道啥情况。实现了你需求功能。OK