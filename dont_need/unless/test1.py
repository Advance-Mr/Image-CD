import tkinter
import tkinter.messagebox as mbox

import func

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
root.title("图片加密程序")

f1 = tkinter.Frame(root)
f1.pack(side=tkinter.TOP, pady=2, fill=tkinter.X)  # 横向占满空间
tkinter.Button(f1, width=3).pack(side=tkinter.LEFT, padx=2)  # 以 f1 做为容器
tkinter.Button(f1, width=3).pack(side=tkinter.LEFT, padx=2)  # 以 f1 做为容器
tkinter.Button(f1, width=3).pack(side=tkinter.LEFT, padx=2)  # 以 f1 做为容器

f3 = tkinter.Frame(root)
f3.pack(side=tkinter.TOP, pady=2, fill=tkinter.BOTH, expand=True)  # 充满窗体剩余空间

#app = wx.App()
#browser = o.FileBrowser(None, title='文件浏览器')
#browser.pack(side=tkinter.LEFT, fill=tkinter.Y)  # 纵向占满空间

f6 = tkinter.LabelFrame(f3, text="书目结构",width=60)  # 以 f3 做为容器
f6.pack(side=tkinter.LEFT, fill=tkinter.Y)  # 纵向占满空间

# choose button created
chooseb = tkinter.Button(f6, text="Choose", command=func.open_img, font=("Arial", 20), bg ="orange", fg ="blue", borderwidth=3, relief="raised")
chooseb.pack(side=tkinter.LEFT, padx=2)


f10 = tkinter.Frame(f6)  # 以 f6 做为容器
f10.pack(side=tkinter.TOP, fill=tkinter.X)

f11 = tkinter.Frame(f6)  # 以 f6 做为容器
f11.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)  # 占满剩余空间


# menu button created
OPTIONS = [
        "abs",
        "Beijing",
        "Shanghai",
        "Tianjin",
        "Aomen",
        "Xianggang",
        "Hankou"
        ]
variable = tkinter.StringVar()
variable.set(OPTIONS[0])
menu = tkinter.OptionMenu(f3, variable, *OPTIONS)
#menu = tkinter.Frame(f3)  # 以 f6 做为容器
menu.pack(side=tkinter.LEFT, pady=2,  expand=True)

f18 = tkinter.Frame(f3)  # 以 f6 做为容器
f18.pack(side=tkinter.LEFT, pady=2, fill=tkinter.BOTH, expand=True)  # 占满剩余空间

# Encrypt button created
enb = tkinter.Button(f18, text="Encrypt",command=func.en_fun, font=("Arial", 20), bg ="light green", fg ="blue", borderwidth=3, relief="raised")
enb.pack(side=tkinter.TOP, padx=2)

# decrypt button created
deb = tkinter.Button(f18, text="Decrypt",command=func.de_fun, font=("Arial", 20), bg ="orange", fg ="blue", borderwidth=3, relief="raised")
deb.pack(side=tkinter.TOP, padx=2)

# reset button created
resetb = tkinter.Button(f18, text="Reset", command=func.reset, font=("Arial", 20), bg ="yellow", fg ="blue", borderwidth=3, relief="raised")
resetb.pack(side=tkinter.TOP, padx=2)

f7 = tkinter.LabelFrame(f3, text="内容预览")  # 以 f3 做为容器
f7.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)  # 纵向占满空间

# save button created
saveb = tkinter.Button(f3, text="Save", command=func.save_img, font=("Arial", 20), bg ="orange", fg ="blue", borderwidth=3, relief="raised")
saveb.pack(side=tkinter.RIGHT, padx=2)

tkinter.Scrollbar(f7, orient=tkinter.VERTICAL).pack(side=tkinter.RIGHT, fill=tkinter.Y)  # 先布局，避免有时被挤掉
tkinter.Text(f7).pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)  # 占满剩余空间

f15 = tkinter.Frame(root)
f15.pack(side=tkinter.TOP, pady=2, fill=tkinter.BOTH, expand=True)  # 充满窗体剩余空间


tkinter.Text(height=30).pack(side=tkinter.TOP, fill=tkinter.X, pady=2)  # 仅1个小部件，所以省掉 Frame 直接使用小部件

def exit_root():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", exit_root)
root.mainloop()