from pymysql import *

class DatabaseHelper():
    @staticmethod
    def get_columns(description):
        #column names are present as the first element of the collection,
        #hence extract the first element[0], create tuple & return it.
        return tuple(map(lambda x:x[0],description))

    @staticmethod
    def get_data(query,parameters=None):
        conn = connect(host='localhost', database='world', user='root', password='vini')
        cur=conn.cursor()
        if(parameters is None):
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        result=cur.fetchone()
        cur.close()
        conn.close()
        return result

    @staticmethod
    def get_all_data(query,parameters=None):
        conn = connect(host='localhost', database='world', user='root', password='vini')
        cur=conn.cursor()
        if(parameters is None):
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        result=cur.fetchall()
        #get me the column names of the data
        headers=DatabaseHelper.get_columns(cur.description)
        cur.close()
        conn.close()
        # add the columns as the first row of my data
        return result

    @staticmethod
    def execute_query(query,parameters=None):
        conn = connect(host='localhost', database='world', user='root', password='vini')
        cur = conn.cursor()
        if(parameters is None):
            cur.execute(query)
        else:
            cur.execute(query,parameters)
        conn.commit()
        cur.close()
        conn.close()

    @staticmethod
    def get_all_data_multiple_input(query,params):
        conn = connect(host='localhost', database='world', user='root', password='vini')
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        cur.execute(query % format_strings,params)
        result= cur.fetchall()
        cur.close()
        conn.close()

        return result

    @staticmethod
    def execute_all_data_multiple_input(query,params):
        conn = connect(host='localhost', database='world', user='root', password='vini')
        cur = conn.cursor()
        format_strings = ','.join(['%s'] * len(params))
        print(format_strings)
        cur.execute(query % format_strings,params)
        conn.commit()
        cur.close()
        conn.close()
