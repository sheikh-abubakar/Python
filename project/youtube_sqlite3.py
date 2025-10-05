import sqlite3

conn = sqlite3.connect('youtube.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)
    

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit

def update_video(vid_id, new_name, time):
    cursor.execute("UPDATE  videos SET name = ?, time = ? WHERE id = ?", (new_name, time, vid_id))
    conn.commit

def delete_video(vid_id):
    cursor.execute("DELETE FROM videos where id = ?", (vid_id,))
    conn.commit

def main():
    while True:
        print("\n Youtube vidoes manager with DataBase: ")
        print("1. List all youtube Videos")
        print("2.  Add a youtube Video")
        print("3. Update  youtube Video")
        print("4. Delete a youtube Video")
        print("5. exit")
        choice = input("enter a choice\n")
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("enter video name: ")
            time = input("enter time stamp: ")
            add_video(name, time)
        elif choice == '3':
            vid_id = input("enter video id: ")
            name = input("enter video name: ")
            time = input("enter time stamp: ")
            update_video(vid_id, name, time)
        elif choice == '4':
            vid_id = input("enter video id: ")
            delete_video(vid_id)
        elif choice == '5':
            break
        else:
            print("invalid choice!!!")

    conn.close()

if __name__ == "__main__":
    main()