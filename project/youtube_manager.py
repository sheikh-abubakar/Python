
def list_all_videos(videos):
    pass

def add_video(video):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


def main():
    videos = []
    while True:
        print("\n youtube Manager")
        print("1. List all youtube Videos")
        print("2.  Add a youtube Video")
        print("3. Update  youtube Video")
        print("4. Delete a youtube Video")
        print("5. exit")
        choice = input("enter a choice\n")

    # just ike switch staatement
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(video)
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