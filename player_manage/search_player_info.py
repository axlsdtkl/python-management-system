from database import Database
from tkinter.messagebox import *


class SearchPlayerInfo(object):
    def __init__(self, player_id,player_name,player_sex,player_age,player_nationaliy, tree_view):
        """模糊查询"""
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        id=player_id.get()
        name = player_name.get()
        sex=player_sex.get()
        age = player_age.get()
        nationality = player_nationaliy.get()
        try:
            if id != '':
                id = int(id)
            else:
                id = 0
            if age != '':
                age = int(age)
            else:
                age = 0

            # 该sql语句筛选出你模糊查询的各种数据（可以组合）
            sql = f'''select * from player where (cast(player_id as char)like '%{id}%' or if(not player_id, NULL, 0) = {id})
            and (player_name like '%{name}%') and(sex like '%{sex}%') and (if(not age, NULL, 0)={age} or cast(age as char) like '%{age}%')
            and(nationality like '%{nationality}%') '''
            # 只有文本框内有有效数据时才执行该语句
            if (id or name or sex or age or nationality) and db.prepare(sql):
                db.update()
                showinfo("提示", "已完成查询")
                player_tuple = db.cursor.fetchall()
                index = db.cursor.description
                for item in player_tuple:
                    row = {}
                    for i in range(len(item)):
                        row[index[i][0]] = item[i]
                    tree_view.insert('', 'end', values=[row['player_id'],row['player_name'],row['sex'],row['age'],row['nationality']])
            else:
                showerror("查询失败", "未查询到相应运动员信息")
        except ValueError:
            showerror("查询失败", "输入不合法")
        db.close()

