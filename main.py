from mysql.connector import MySQLConnection, Error
        
def make_connection():
    try:
        conn = MySQLConnection(host='localhost',
                               database='school',
                               user='root',
                               password='seekrit')
        
        if conn.is_connected():
            print('Connected to the MySQL database!')
            
            return conn
                
    except Error as e:
        print('Connection failed.')
        print(e)
        
        return None
    
def do_query(sql):
    cursor = None
    
    # Connect to the database.
    conn = make_connection()
    
    if conn != None:
        try:
            # Do the query.
            cursor = conn.cursor()
            cursor.execute(sql);
            
        except Error as e:
            print('Query failed')
            print(e)
            
            return [(), 0]

    # Return the fetched data as a list of tuples,
    # one tuple per table row.
    if conn != None:
        rows = cursor.fetchall()
        count = cursor.rowcount
            
        conn.close()
        print('Connection closed.')
        
        return [rows, count]
    else:
        return [(), 0]

def do_queries():
    sql1 = "SELECT * FROM Class";
    
    print(sql1)
    print()
    
    rows, count = do_query(sql1)
    
    print()
    print(f'Fetched {count} rows.')
    print(rows)
    print()
    
    for row in rows:
        print(row)
        
    print()
    print('--------------------------------------------------')
    print()
    
    sql2 = "SELECT code, subject \n" \
         + "FROM teacher, class \n" \
         + "WHERE last = 'Flynn' \n" \
         + "AND first = 'Mabel' \n" \
         + "AND id = teacher_id";
    
    print(sql2)
    print()
    
    rows, count = do_query(sql2)
    
    print()
    for row in rows:
        print(row)
    
if __name__ == '__main__':
    do_queries()
    