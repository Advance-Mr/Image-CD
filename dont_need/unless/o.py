import os
import wx


class FileBrowser(wx.Frame):
    def __init__(self, parent, title):
        super(FileBrowser, self).__init__(parent, title=title, size=(400, 300))

        # 创立面板
        panel = wx.Panel(self)

        # 创建目录控件
        self.dir_ctrl = wx.GenericDirCtrl(panel, dir=wx.GetHomeDir(), style=wx.DIRCTRL_DIR_ONLY)

        #创立个sizer
        sizer = wx.BoxSizer(wx.VERTICAL)

        # 将目录控件添加到sizer里
        sizer.Add(self.dir_ctrl, 1, wx.EXPAND)

        # 创立个工具条
        toolbar = self.CreateToolBar()
        toolbar.SetToolBitmapSize((16, 16))

        # 增加新建文件夹按钮
        new_folder_bmp = wx.ArtProvider.GetBitmap(wx.ART_NEW_DIR, wx.ART_TOOLBAR, (16, 16))
        new_folder_tool = toolbar.AddTool(wx.ID_NEW, '新文件夹', new_folder_bmp)
        self.Bind(wx.EVT_TOOL, self.OnNewFolder, new_folder_tool)

        # 增加拷贝按钮
        copy_bmp = wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_TOOLBAR, (16, 16))
        copy_tool = toolbar.AddTool(wx.ID_COPY, '拷贝', copy_bmp)
        self.Bind(wx.EVT_TOOL, self.OnCopy, copy_tool)

        # 增加剪切按钮
        cut_bmp = wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_TOOLBAR, (16, 16))
        cut_tool = toolbar.AddTool(wx.ID_CUT, '剪切', cut_bmp)
        self.Bind(wx.EVT_TOOL, self.OnCut, cut_tool)

        # 增加粘贴按钮
        paste_bmp = wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_TOOLBAR, (16, 16))
        paste_tool = toolbar.AddTool(wx.ID_PASTE, '粘贴', paste_bmp)
        self.Bind(wx.EVT_TOOL, self.OnPaste, paste_tool)

        # 增加删除按钮
        delete_bmp = wx.ArtProvider.GetBitmap(wx.ART_DELETE, wx.ART_TOOLBAR, (16, 16))
        delete_tool = toolbar.AddTool(wx.ID_DELETE, '删除', delete_bmp)
        self.Bind(wx.EVT_TOOL, self.OnDelete, delete_tool)

        # 增加重命名按钮
        rename_bmp = wx.ArtProvider.GetBitmap(wx.ART_EDIT, wx.ART_TOOLBAR, (16, 16))
        rename_tool = toolbar.AddTool(wx.ID_ANY, '重命名', rename_bmp)
        self.Bind(wx.EVT_TOOL, self.OnRename, rename_tool)

        # 增加打开文件按钮
        open_file_bmp = wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR, (16, 16))
        open_file_tool = toolbar.AddTool(wx.ID_OPEN, '打开文件', open_file_bmp)
        self.Bind(wx.EVT_TOOL, self.OnOpenFile, open_file_tool)

        # 完成工具条的设置
        toolbar.Realize()

        # 设置面板的尺寸
        panel.SetSizer(sizer)
        # 显示框架
        self.Show()

    def OnNewFolder(self, event):
        dlg = wx.TextEntryDialog(self, '为文件夹起个新名字', '新文件夹')

        if dlg.ShowModal() == wx.ID_OK:
            path = self.dir_ctrl.GetPath()
            name = dlg.GetValue()
            folder_path = os.path.join(path, name)

            if os.path.exists(folder_path):
                wx.MessageBox('这个文件夹已经存在', '失败', wx.OK | wx.ICON_ERROR)
            else:
                os.mkdir(folder_path)

                # 刷新目录控件
                self.dir_ctrl.ReCreateTree()

    def OnCopy(self, event):
        pass

    def OnCut(self, event):
        pass

    def OnPaste(self, event):
        pass

    def OnDelete(self, event):
        path = self.dir_ctrl.GetPath()

        for item in self.dir_ctrl.GetSelections():
            item_path = os.path.join(path, item.GetText())

            if os.path.isdir(item_path):
                dlg = wx.MessageDialog(self,
                                       '你确定要删除这个文件夹和它的所有内容吗？',
                                       '确认删除',
                                       wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)

                if dlg.ShowModal() == wx.ID_YES:
                    try:
                        os.rmdir(item_path)
                    except OSError as e:
                        wx.MessageBox(str(e), '错误', wx.OK | wx.ICON_ERROR)
            else:
                dlg = wx.MessageDialog(self,
                                       '你确定要删除这个文件吗？',
                                       '确认删除',
                                       wx.YES_NO | wx.NO_DEFAULT | wx.ICON_WARNING)

                if dlg.ShowModal() == wx.ID_YES:
                    try:
                        os.remove(item_path)
                    except OSError as e:
                        wx.MessageBox(str(e), '错误', wx.OK | wx.ICON_ERROR)

        # 刷新目录控件
        self.dir_ctrl.ReCreateTree()

    def OnRename(self, event):
        path = self.dir_ctrl.GetPath()

        for item in self.dir_ctrl.GetSelections():
            item_path = os.path.join(path, item.GetText())

            dlg = wx.TextEntryDialog(self,
                                     '输入这个项目的新名称：',
                                     '新项目名称',
                                     value=item.GetText())

            if dlg.ShowModal() == wx.ID_OK:
                new_name = dlg.GetValue()
                new_path = os.path.join(path, new_name)

                try:
                    os.rename(item_path, new_path)
                except OSError as e:
                    wx.MessageBox(str(e), 'Error', wx.OK | wx.ICON_ERROR)

        # 刷新目录控件
        self.dir_ctrl.ReCreateTree()

    def OnOpenFile(self, event):
        path = self.dir_ctrl.GetPath()

        for item in self.dir_ctrl.GetSelections():
            item_path = os.path.join(path, item.GetText())

            if os.path.isfile(item_path):
                os.startfile(item_path)


if __name__ == '__main__':
    app = wx.App()
    browser = FileBrowser(None, title='文件浏览器')
    browser.SetSize((800, 600))  # 设置窗口大小to 800x600
    browser.Show()
    app.MainLoop()