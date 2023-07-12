import MySQLdb

class SQL_Connect:
    def __init__(self):
        self.sql = MySQLdb.connect(
                        host='localhost',
                        user='danwang',
                        passwd='dangina926',
                        db ='animate_web',
                    )
        self.cursor = self.sql.cursor()

    def select(self, ):
        cursor = self.cursor
        
        query = 'SELECT * FROM animate_info Where {};'.format()
        cursor.execute(query)
