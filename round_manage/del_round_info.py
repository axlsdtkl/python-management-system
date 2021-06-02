from database import Database
from tkinter.messagebox import *
from .show_round_info import ShowRoundInfo

class DelRoundInfo(object):
    def __init__(self, tree_view, match_id,round_id,round_name,start_time):
        """模糊删除"""
        db = Database()
        round_id=round_id.get()
        round_name=round_name.get()
        start_time=start_time.get()
        try:
            sql = f'''select * from round_table where (cast(round_id as char)like '%{round_id}%' or if(not round_id, NULL, 0) = {round_id}) '''
            if (round_id):
                if not(db.prepare(sql)):
                    showerror("删除失败", "未查询到该小局信息")
                    return
                db.update()
                round_tuple = db.cursor.fetchall()
                index = db.cursor.description
                for item in round_tuple:
                    row = {}
                    for i in range(len(item)):
                        row[index[i][0]] = item[i]
                    if askokcancel("提示", f"是否删除该比赛的信息(小局编号:{row['round_id']} 比赛名称:{row['round_name']} 比赛时间:{row['start_time']})"):
                        sql=f"delete from round_table where (cast(round_id as char)like '%{round_id}%' or if(not round_id, NULL, 0) = {round_id})"
                        db.prepare(sql)
                        db.update()
                        showinfo("提示", "删除成功")
                        ShowRoundInfo(tree_view,match_id)
            else:
                showerror("删除失败", "未查询到该小局信息")
        except ValueError:
            showerror("删除失败", "输入非法")