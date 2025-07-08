import json


def load_data():
    try:
        with open("youtube.txt", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']} ")

    print("\n")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name' : name, 'time' : time})
    save_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to update; "))
    if 1 <= index <= len(videos):
        new_name = input("Enter the new video name: ")
        new_time = input("Enter the new video time: ")
        videos[index-1] = {'name':new_name, 'time':new_time}
        save_data(videos)
    else:
        print("Invalid index...")
def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video index to delete. "))
    
    if 1<= index <= len(videos):
        del videos[index-1]
        save_data(videos)
    else:
        print("Invalid index.")


def main():
    videos = load_data()
    while True:
        print("Youtube Manager---| Choose an option. ")
        print("1. List all videos ")
        print("2. Add video ")
        print("3. Update video details ")
        print("4. Delete video")
        print("5. Exit....")
        choice = input("Enter your choice: ")
        print(videos)

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
                print("Invalid choice...")


if __name__ == "__main__":
    main()