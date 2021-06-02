from tkinter import *
from .player_win import *
from .match_win import *

class Index:
    def __init__(self):
        """创建登录界面"""
        # 创建主窗口,用于容纳其它组件
        self.index_root=Tk()
        # 给主窗口设置标题内容
        self.index_root.title("智能亚运数据采集管理系统-羽毛球类")
        # 设置窗口大小和位置
        screenwidth=self.index_root.winfo_screenwidth()
        screenheight=self.index_root.winfo_screenheight()
        width=700
        high=600

        self.index_root.geometry('%dx%d+%d+%d'%(width,high,(screenwidth-width)/2,(screenheight-high)/2))

        # 创建画布
        #self.image_file = PhotoImage(file="badminton_bg.png")
        # 加载图片文件，并将图片置于画布上
        #self.image = self.canvas.create_image(0, 0, anchor='nw', image=self.image_file)
        # 放置画布（为上端）


        Label(self.index_root, text='智能亚运数据采集管理系统-羽毛球类', bg='white', fg='red', font=('宋体', 20)).pack(side=TOP, fill='x')
        # 创建一个相机配置检查模块功能与操作的按钮
        Button(self.index_root, command=lambda: self.camera_configuration_check(), text="相机配置与检查", width=30).place(x=230, y=120)
        # 创建一个赛数据录制模块功能与操作的按钮
        Button(self.index_root, command=lambda: self.competion_record(), text="比赛数据录制", width=30).place(x=230, y=180)
        # 比赛信息管理模块功能与操作
        Button(self.index_root, command=lambda: self.competion_record(), text="比赛回放管理", width=30).place(x=230, y=240)
        # 选手信息管理模块功能与操作
        Button(self.index_root, command=lambda: self.player_information_manage(), text="选手信息管理", width=30).place(x=230, y=300)
        mainloop()
    #def camera_configuration_check(self):
    #def competion_record(self):
    def player_information_manage(self):
        #self.index_root.destroy()
        Player_Win()
    def competion_record(self):
        Match_Manage()

