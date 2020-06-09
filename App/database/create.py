import database.connect as database

# CREATE DB IF NOT EXISTS AND ONE TABLE FOR Authors, ONE FOR BOOKS  
# AND ONE TABLE TO REFERENCE THEM


def createDB():
    conn = database.connect_to_DB()

    conn.cursor().execute("CREATE DATABASE IF NOT EXISTS Library")
    conn.connect(database="Library")

    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Authors 
                        (ID INT AUTO_INCREMENT PRIMARY KEY,
                        Name VARCHAR(256) );''')
    
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS Books
                        (ID INT PRIMARY KEY,
                        ISBN VARCHAR(17),
                        Title VARCHAR(256),
                        PublishedDate DATE);''')
    
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS AuthorsBooks
                        (ID_b INT,
                        ID_auth INT,
                        PRIMARY KEY (ID_b, ID_auth),
                        FOREIGN KEY (ID_b) REFERENCES Books(ID),
                        FOREIGN KEY (ID_auth) REFERENCES Authors(ID) );''')

    conn.cursor().execute('''CREATE INDEX Authors_name
                          ON Authors (Name)''')

    conn.cursor().execute('''CREATE INDEX Books_name
                          ON Books (Title)''')
