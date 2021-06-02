from database import Database
from tkinter.messagebox import *
from .show_player_info import ShowPlayerInfo

class ModifyPlayerInfo(object):
    def __init__(self, tree_view,player_id,player_name,player_sex,player_age,plager_nationality):
        """修改学生信息"""
        db = Database()
        id_str = str(player_id.get())
        name = player_name.get()
        #print(id)
        try:
            if not (id_str.strip() and name.strip()):
                raise ValueError
            id= int(id_str)
            sex = player_sex.get()
            #age = int(player_age.get())
            if(player_age.get().strip()):
                age = int(player_age.get())
            else:
                age=0

            nationality=plager_nationality.get()

            if db.prepare(f"select * from player where player_id={id}") != 0:
                db.prepare(f"update player set player_id={id},player_name='{name}', sex='{sex}',"
                           f"age={age},nationality='{nationality}' where player_id='{id}'")
                db.update()
                showinfo("提示", "修改成功")
                ShowPlayerInfo(tree_view)
            else:
                showerror("修改失败", "未查询到该参赛选手信息")
        except ValueError:
            showerror("修改失败", "信息未填写完整或者输入不合法")
        db.close()
