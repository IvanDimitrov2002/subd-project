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
                        (ISBN VARCHAR(17),
                        Title VARCHAR(256),
                        PublishedDate DATE,
                        PRIMARY KEY (ISBN));''')
    
    conn.cursor().execute('''CREATE TABLE IF NOT EXISTS AuthorsBooks
                        (ISBN_b VARCHAR(17),
                        ID_auth INT,
                        PRIMARY KEY (ISBN, ID_auth),
                        FOREIGN KEY (ISBN_B) REFERNCES Books(ISBN),
                        FOREING KEY (ID_auth) REFERENCES Authors(ID));''')
