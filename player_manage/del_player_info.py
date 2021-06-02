from database import Database
from tkinter.messagebox import *
from .show_player_info import ShowPlayerInfo

class DelPlayerInfo(object):
    def __init__(self, tree_view, player_id, player_name, player_sex, player_age,player_nationality):
        """模糊删除"""
        db = Database()
        id = player_id.get()
        name = player_name.get()
        sex = player_sex.get()
        age = player_age.get()
        nationality=player_nationality.get()
        try:
            if id != '':
                id = int(id)
            else:
                id = 0
            if age != '':
                age = int(age)
            else:
                age = 0
            sql = f'''select * from player where (cast(player_id as char)like '%{id}%' or if(not player_id, NULL, 0) = {id}) 
                    and (player_name like '%{name}%') and
                    (sex like '%{sex}%') and (cast(age as char) like '%{age}%' or if(not age, NULL, 0)={age})
                    and(nationality like '%{nationality}%')'''

            if (id or name or sex or age or nationality):
                if not(db.prepare(sql)):
                    showerror("删除失败", "未查询到该运动员信息")
                    return
                db.update()
                player_tuple = db.cursor.fetchall()
                index = db.cursor.description
                for item in player_tuple:
                    row = {}
                    for i in range(len(item)):
                        row[index[i][0]] = item[i]
                    if askokcancel("提示", f"是否删除该运动员的信息(编号:{row['player_id']} 姓名:{row['player_name']} 性别:{row['sex']} 年龄:{row['age']} 国籍:{row['nationality']})"):
                        sql=f"delete from player where (cast(player_id as char)like '%{id}%' or if(not player_id, NULL, 0) = {id})and (player_name like '%{name}%') and(sex like '%{sex}%') and (if(not age, NULL, 0)={age} or cast(age as char) like '%{age}%')and(nationality like '%{nationality}%')  limit 1"
                        db.prepare(sql)
                        db.update()
                        showinfo("提示", "删除成功")
                        ShowPlayerInfo(tree_view)
            else:
                showerror("删除失败", "未查询到该运动员信息")
        except ValueError:
            showerror("删除失败", "输入非法")