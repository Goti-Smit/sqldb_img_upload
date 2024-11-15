import sqlite3




conn = sqlite3.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS images (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    image BLOB

                )''')


with open('/home/elit/DB_img_upload/mydatabase.db-x-images-1-image.jpg', 'rb') as f:

    image_data = f.read()

cursor.execute("INSERT INTO images (image) VALUES (?)", (image_data,)) 

conn.commit()

conn.close()
