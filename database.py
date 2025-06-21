import sqlite3
## tha main function for creating the required table
def init_db():
    ## Connect to the SQlite db and create one if it doesn't exist
    connect = sqlite3.connect('flights.db')
    cursor = connect.cursor()

    ## Excute SQL commands by creating the reservation table
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS reservations (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NOT NULL,
                   flight_number TEXT NOT NULL,
                   departure TEXT NOT NULL,
                   destination TEXT NOT NULL,
                   date TEXT NOT NULL,
                   seat_number TEXT NOT NULL
                )
            ''')
                
    
    ## commit the changes and close the database connection
    connect.commit()
    connect.close()