from database import Database
from tkinter.messagebox import *
from .show_match_info import *

class DelMatchInfo(object):
    def __init__(self, tree_view, match_id):
        """模糊删除"""
        db = Database()
        id = match_id.get()
        try:
            if id != '':
                id = int(id)
            else:
                id = 0
            sql = f'''select * from match_table where (cast(match_id as char)like '%{id}%' or if(not match_id, NULL, 0) = {id}) '''
            if (id):
                if not(db.prepare(sql)):
                    showerror("删除失败", "未查询到该比赛信息")
                    return
                db.update()
                match_tuple = db.cursor.fetchall()
                index = db.cursor.description
                for item in match_tuple:
                    row = {}
                    for i in range(len(item)):
                        row[index[i][0]] = item[i]
                    if askokcancel("提示", f"是否删除该比赛的信息(比赛编号:{row['match_id']} 比赛名称:{row['match_name']} 比赛时间:{row['start_time']} 比赛类型:{row['type']})"):
                        sql=f"delete from match_table where (cast(match_id as char)like '%{id}%' or if(not match_id, NULL, 0) = {id})"
                        db.prepare(sql)
                        db.update()
                        showinfo("提示", "删除成功")
                        ShowMatchInfo(tree_view)
            else:
                showerror("删除失败", "未查询到该运动员信息")
        except ValueError:
            showerror("删除失败", "输入非法")