from database import Database

class ShowMatchInfo(object):
    def __init__(self, tree_view):
        db = Database()
        x = tree_view.get_children()
        for item in x:
            tree_view.delete(item)
        db.cursor.execute("select * from match_table")
        match_tuple = db.cursor.fetchall()
        #列名
        index = db.cursor.description
        #print(index)
        for item in match_tuple:
            row={}
            for i in range(len(item)):
                row[index[i][0]]=item[i]
            #print(row)
            tree_view.insert("", 'end', values=[row['match_id'],row['match_name'],row['start_time'],row['type'],row['playerA_id'],row['playerC_id']])