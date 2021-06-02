from database import Database


class ShowPlayerInfo(object):
    def __init__(self, tree_view):
        """将所有运动员信息显示在表格上"""
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        db.cursor.execute("select * from player")
        player_tuple = db.cursor.fetchall()
        #列名
        index = db.cursor.description
        #print(index)
        for item in player_tuple:
            row={}
            for i in range(len(item)):
                row[index[i][0]]=item[i]
            #print(row)
            tree_view.insert("", 'end', values=[row['player_id'],row['player_name'],row['sex'],row['age'],row['nationality']])