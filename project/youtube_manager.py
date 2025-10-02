import json

def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file) # convert to json
    except FileNotFoundError: #type mentioned
        return []
    
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file) # whata to write, wheer to write

def list_all_videos(videos):
    # to add indexing we can use enum
    for index, video in enumerate(videos, start=1):
        print(f"{index}. ")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video timeStamp: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass



def main():
    videos = []
    videos = load_data()
    
    while True:
        print("\n youtube Manager")
        print("1. List all youtube Videos")
        print("2.  Add a youtube Video")
        print("3. Update  youtube Video")
        print("4. Delete a youtube Video")
        print("5. exit")
        choice = input("enter a choice\n")
        print(videos)

    # just ike switch staatement
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__": #dender
    main() 