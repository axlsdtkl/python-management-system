from database import Database


class ShowRoundInfo(object):
    def __init__(self, tree_view,match_id):
        """将所有运动员信息显示在表格上"""
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        print(match_id)
        db.cursor.execute(f"select * from round_table where match_id={match_id}")
        round_tuple = db.cursor.fetchall()
        #列名
        index = db.cursor.description
        #print(index)
        for item in round_tuple:
            row={}
            for i in range(len(item)):
                row[index[i][0]]=item[i]
            #print(row)
            tree_view.insert("", 'end', values=[row['round_name'],row['start_time'],row['round_id'],row['match_id']])